package main

import (
	"bssweb.bsstudio.hu/file-api/internal/controller"
	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()

	healthController := controller.HealthController{}
	healthController.SetupRouter(router)

	api := router.Group("/api/v1")
	{
		memberController := controller.MemberController{}
		memberController.SetupRouter(api)

		videoController := controller.VideoController{}
		videoController.SetupRouter(api)
	}

	if err := router.Run(); err != nil {
		panic(err)
	}
}
