from fastapi import FastAPI, HTTPException
from typing import List, Dict, Any
import pandas as pd


app = FastAPI()

# Se cargan los dataframes globalmente
df_dev = pd.read_parquet(r"3. BD_API/endpoint_1.parquet")
df_userdata= pd.read_parquet(r"3. BD_API/endpoint_2.parquet")
df_genredata=pd.read_parquet(r"3. BD_API/endpoint_3.parquet")
df_topdev=pd.read_parquet(r"3. BD_API/endpoint_4_5.parquet")
df_dev_sentiment=pd.read_parquet(r"3. BD_API/endpoint_4_5.parquet")

# 1. Endpoint: Developer Data
@app.get("/developer/")
def developer(developer: str) -> List[Dict[str, Any]]:
    df_filtrado = df_dev[df_dev['developer'] == developer]
    if df_filtrado.empty:
        raise HTTPException(status_code=404, detail=f"No se encontraron datos para el developer: {developer}")

    conteo_apps = df_filtrado.groupby('year')['app_name'].count().reset_index()
    conteo_apps = conteo_apps.rename(columns={'app_name': 'Cantidad de Ítems'})

    gratuitas = df_filtrado[df_filtrado['price'] == 0].groupby('year')['app_name'].count()
    total_por_año = df_filtrado.groupby('year')['app_name'].count()
    porcentaje_gratis = (gratuitas / total_por_año * 100).reset_index(name='Contenido Free')

    resultado = pd.merge(conteo_apps, porcentaje_gratis, on='year', how='left').fillna(0)
    resultado['Contenido Free'] = resultado['Contenido Free'].astype(int).astype(str) + '%'

    return resultado.to_dict(orient='records')


# 2. Endpoint: User Data
@app.get("/userdata/")
def userdata(user_id: str) -> Dict[str, Any]:
    user_data = df_userdata[df_userdata['user_id'] == user_id]
    if user_data.empty:
        raise HTTPException(status_code=404, detail=f"No se encontraron datos para el usuario: {user_id}")

    total_spent = user_data['price'].sum()
    recommend_percentage = (user_data['recommend'].mean()) * 100
    total_items = user_data['item_id'].nunique()

    return {
        "User_id": user_id,
        "Total_gastado": round(total_spent, 2),
        "%_recomendacion": round(recommend_percentage, 2),
        "Cantidad_items": total_items
    }

# 3. Endpoint: User for Genre
@app.get("/userforgenre/")
def UserForGenre(genero: str) -> Dict[str, Any]:
    genre_data = df_genredata[df_genredata['genres'] == genero]
    if genre_data.empty:
        raise HTTPException(status_code=404, detail=f"No se encontraron datos para el género: {genero}")

    horas_por_usuario = genre_data.groupby('user_id')['playtime_forever_hours'].sum()
    max_jugador = horas_por_usuario.idxmax()
    datos_jugador = genre_data[genre_data['user_id'] == max_jugador]

    horas_por_año = datos_jugador.groupby('year')['playtime_forever_hours'].sum().reset_index()
    max_usuario_año_playtime_list = [
        {"Año": int(year), "Horas": float(hours)}
        for year, hours in zip(horas_por_año['year'], horas_por_año['playtime_forever_hours'].round(1))
    ]

    return {
        "Género": genero,
        "Usuario": max_jugador,
        "Horas_jugadas_por_año": max_usuario_año_playtime_list
    }



# 4. Endpoint: Top 3 Developers by Year
@app.get("/top3_developers_by_year/")
def top3_developers_by_year(year: int) -> List[Dict[str, Any]]:
    df_year = df_topdev[df_topdev['year'] == year]
    if df_year.empty:
        raise HTTPException(status_code=404, detail=f"No se encontraron juegos para el año {year}")

    df_recommended = df_year[df_year['true_recommend'] == True]
    top_developers = (
        df_recommended.groupby('developer')['item_name']
        .nunique()
        .sort_values(ascending=False)
        .head(3)
    )

    return [
        {f"Puesto {i + 1}": developer}
        for i, developer in enumerate(top_developers.index)
    ]

# 5. Endpoint: Developer Reviews Analysis
@app.get("/developer_reviews_analysis/")
def developer_reviews_analysis(desarrollador: str) -> Dict[str, Any]:
    developer_df = df_dev_sentiment[df_dev_sentiment['developer'] == desarrollador]
    if developer_df.empty:
        raise HTTPException(status_code=404, detail=f"No hay registros para el desarrollador: {desarrollador}")

    negative_count = developer_df[developer_df['sentiment_analysis'] == 0].shape[0]
    positive_count = developer_df[developer_df['sentiment_analysis'] == 1].shape[0]

    return {
        desarrollador: [f"Negative = {negative_count}", f"Positive = {positive_count}"]
    }

