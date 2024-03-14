package model

type Member struct {
	Id  string `json:"id" binding:"required"`
	Url string `json:"url" binding:"required"`
}

type Video struct {
	Id  string
	Url string
}
