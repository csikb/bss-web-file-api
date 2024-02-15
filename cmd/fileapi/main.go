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

	api := router.Group("/api/v1")
	{
		memberController := controller.MemberController{}
		{
			member := api.Group("/member")
			{
				member.POST("/", memberController.Create)
				member.PUT("/", memberController.Update)
				member.DELETE("/", memberController.Archive)
			}
		}

		videoController := controller.VideoController{}
		{
			video := api.Group("/video")
			{
				video.POST("/", videoController.Create)
				video.PUT("/", videoController.Update)
				video.DELETE("/", videoController.Archive)
			}
		}
	}

	if err := router.Run(); err != nil {
		panic(err)
	}
}
