package controller

import (
	"bssweb.bsstudio.hu/file-api/internal/model"
	"github.com/gin-gonic/gin"
	"net/http"
)

type VideoController struct{}

func (ctrl *VideoController) Create(context *gin.Context) {
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

func (ctrl *VideoController) Update(context *gin.Context) {
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

func (ctrl *VideoController) Archive(context *gin.Context) {
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
