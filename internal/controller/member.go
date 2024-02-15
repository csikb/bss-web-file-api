package controller

import (
	"bssweb.bsstudio.hu/file-api/internal/model"
	"bssweb.bsstudio.hu/file-api/internal/service"
	"github.com/gin-gonic/gin"
	"net/http"
)

type MemberController struct {
	memberService service.MemberService
}

func (ctrl *MemberController) Create(context *gin.Context) {
	var member model.Member
	if err := context.ShouldBindJSON(&member); err != nil {
		context.JSON(
			http.StatusBadRequest,
			gin.H{
				"error":   "Failed to parse request body",
				"message": err.Error(),
			},
		)
		return
	}

	if err := ctrl.memberService.Create(member); err != nil {
		context.JSON(
			http.StatusInternalServerError,
			gin.H{
				"error":   "Failed to create member",
				"message": err.Error(),
			},
		)
		return
	}

	context.JSON(http.StatusCreated, member)
}

func (ctrl *MemberController) Update(context *gin.Context) {
	var member model.Member
	if err := context.ShouldBindJSON(&member); err != nil {
		context.JSON(
			http.StatusBadRequest,
			gin.H{
				"error":   "Failed to parse request body",
				"message": err.Error(),
			},
		)
		return
	}

	if err := ctrl.memberService.Update(member); err != nil {
		context.JSON(
			http.StatusInternalServerError,
			gin.H{
				"error":   "Failed to update member",
				"message": err.Error(),
			},
		)
		return
	}

	context.JSON(http.StatusOK, member)
}

func (ctrl *MemberController) Archive(context *gin.Context) {
	var member model.Member
	if err := context.ShouldBindJSON(&member); err != nil {
		context.JSON(
			http.StatusBadRequest,
			gin.H{
				"error":   "Failed to parse request body",
				"message": err.Error(),
			},
		)
		return
	}

	if err := ctrl.memberService.Archive(member); err != nil {
		context.JSON(
			http.StatusInternalServerError,
			gin.H{
				"error":   "Failed to archive member",
				"message": err.Error(),
			},
		)
		return
	}

	context.JSON(http.StatusOK, member)
}
