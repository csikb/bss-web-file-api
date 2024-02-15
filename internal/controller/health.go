package controller

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

type HealthController struct {
}

func (ctrl *HealthController) SetupRouter(router *gin.Engine) {
	actuator := router.Group("/actuator")
	{
		actuator.GET("/ping", ctrl.ping)
		actuator.GET("/health", ctrl.health)
	}
}

func (ctrl *HealthController) ping(context *gin.Context) {
	context.String(200, "Pong")
}

func (ctrl *HealthController) health(context *gin.Context) {
	context.String(http.StatusOK, "UP")
}
