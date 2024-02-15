package config

import (
	"github.com/spf13/viper"
	"os"
	"path/filepath"
)

type Config struct {
	BasePath string
}

var DefaultConfig = newConfig()

func newConfig() Config {
	v := viper.New()
	{
		v.SetDefault("BASE_PATH", "$HOME/fileapi")
		v.AutomaticEnv()
		if err := v.BindEnv("BASE_PATH"); err != nil {
			panic(err)
		}
	}

	basePath := os.ExpandEnv(v.GetString("BASE_PATH"))

	absBasePath, err := filepath.Abs(basePath)
	if err != nil {
		panic(err)
	}

	return Config{
		BasePath: absBasePath,
	}
}
