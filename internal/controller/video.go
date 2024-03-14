package controller

import (
	"bssweb.bsstudio.hu/file-api/internal/model"
	"github.com/gin-gonic/gin"
	"net/http"
)

type VideoController struct{}

func (ctrl *VideoController) SetupRouter(api *gin.RouterGroup) {
	video := api.Group("/video")
	{
		video.POST("/", ctrl.create)
		video.PUT("/", ctrl.update)
		video.DELETE("/", ctrl.archive)
	}
}

func (ctrl *VideoController) create(context *gin.Context) {
	var video model.Video
	if err := context.ShouldBindJSON(&video); err != nil {
		context.JSON(
			http.StatusBadRequest,
			gin.H{
				"error":   "Failed to parse request body",
				"message": err.Error(),
			},
		)
		return
	}
}

func (ctrl *VideoController) update(context *gin.Context) {
	var video model.Video
	if err := context.ShouldBindJSON(&video); err != nil {
		context.JSON(
			http.StatusBadRequest,
			gin.H{
				"error":   "Failed to parse request body",
				"message": err.Error(),
			},
		)
		return
	}
}

func (ctrl *VideoController) archive(context *gin.Context) {
	var video model.Video
	if err := context.ShouldBindJSON(&video); err != nil {
		context.JSON(
			http.StatusBadRequest,
			gin.H{
				"error":   "Failed to parse request body",
				"message": err.Error(),
			},
		)
		return
	}
}
