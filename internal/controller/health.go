package controller

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

type HealthController struct {
	context gin.Context
}

func (ctrl *HealthController) Ping(context *gin.Context) {
	context.String(200, "Pong")
}

func (ctrl *HealthController) Health(context *gin.Context) {
	context.String(http.StatusOK, "UP")
}
