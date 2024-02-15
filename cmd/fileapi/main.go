package main

import (
	"bssweb.bsstudio.hu/file-api/internal/controller"
	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()

	healthController := controller.HealthController{}
	{
		actuator := router.Group("/actuator")
		{
			actuator.GET("/ping", healthController.Ping)
			actuator.GET("/health", healthController.Health)
		}
	}

	memberController := controller.MemberController{}
	{
		member := router.Group("/member")
		{
			member.POST("/", memberController.Create)
			member.PUT("/", memberController.Update)
			member.DELETE("/", memberController.Archive)
		}
	}

	videoController := controller.VideoController{}
	{
		video := router.Group("/video")
		{
			video.POST("/", videoController.Create)
			video.PUT("/", videoController.Update)
			video.DELETE("/", videoController.Archive)
		}
	}

	if err := router.Run(); err != nil {
		panic(err)
	}
}
