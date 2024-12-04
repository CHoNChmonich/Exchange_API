from fastapi import FastAPI, HTTPException, Query
import httpx

app = FastAPI(title="Currency Converter API", version="1.0.0")

# Новый URL для API
EXCHANGE_RATE_API = "https://open.er-api.com/v6/latest"

@app.get("/api/v1/rates", summary="Конвертация валюты", description="Конвертирует валюту, используя актуальные курсы обмена.")
async def convert_currency(
    from_currency: str = Query(..., alias="from", description="Валюта, из которой конвертировать (например, USD)"),
    to_currency: str = Query(..., alias="to", description="Валюта, в которую конвертировать (например, RUB)"),
    value: float = Query(..., gt=0, description="Сумма для конвертации (например, 1.0)")
):
    """
    Конвертирует валюту, используя актуальные курсы с внешнего API.
    """
    try:
        # Отправка запроса к новому API
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{EXCHANGE_RATE_API}/{from_currency}")
            response.raise_for_status()
            data = response.json()

        # Проверка, что необходимая валюта присутствует в данных
        rates = data.get("rates")
        if not rates or to_currency not in rates:
            raise HTTPException(status_code=404, detail=f"Курс обмена не найден для валют: {from_currency} в {to_currency}")

        # Вычисление результата
        exchange_rate = rates[to_currency]
        result = value * exchange_rate
        return {"result": round(result, 2)}

    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при запросе к внешнему API: {e}")
    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Произошла непредвиденная ошибка: {e}")
