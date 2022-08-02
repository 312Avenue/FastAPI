from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi_pagination import add_pagination
from sqladmin import Admin
from starlette.responses import JSONResponse

from app.database import engine
from app.admin import CategoryAdmin, PostAdmin, TagAdmin, UserAdmin
from app.routers import router


app = FastAPI()

admin = Admin(app, engine)


@app.exception_handler(RequestValidationError)
def validation_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content=jsonable_encoder({'detail': exc.errors()})
    )


app.include_router(router)
add_pagination(app)


# TODO: Docker
# TODO: Deploy


admin.register_model(CategoryAdmin)
admin.register_model(PostAdmin)
admin.register_model(TagAdmin)
admin.register_model(UserAdmin)
