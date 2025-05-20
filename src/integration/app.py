from fastapi import FastAPI, HTTPException, Query
from .main import get_informacion_historica, get_trabajadores, get_representantes_legales
 
app = FastAPI()

@app.get("/informacion-historica")
async def get_informacion_historica_endpoint(ruc: str = Query(..., description="El número de RUC que deseas consultar")):
    try:
        return get_informacion_historica(ruc)
    except ValueError:
        raise HTTPException(status_code=400, detail="RUC inválido")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/trabajadores")
async def get_trabajadores_endpoint(ruc: str = Query(..., description="El número de RUC que deseas consultar")):
    try:
        return get_trabajadores(ruc)
    except ValueError:
        raise HTTPException(status_code=400, detail="RUC inválido")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/representantes-legales")
async def get_representantes_legales_endpoint(ruc: str = Query(..., description="El número de RUC que deseas consultar")):
    try:
        return get_representantes_legales(ruc)
    except ValueError:
        raise HTTPException(status_code=400, detail="RUC inválido")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))