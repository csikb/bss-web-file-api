package service

import (
	"bssweb.bsstudio.hu/file-api/internal/config"
	"bssweb.bsstudio.hu/file-api/internal/model"
	"fmt"
	"os"
	"path/filepath"
)

type MemberService struct {
}

var basePath = config.DefaultConfig.BasePath

func (service *MemberService) Create(member model.Member) error {
	// Create the member directory
	memberDir := basePath + "/m/" + member.Id
	if err := os.MkdirAll(memberDir, 0755); err != nil {
		return err
	}

	err2 := service.createFolderIfItDoesNotExist(basePath + "/member")
	if err2 != nil {
		return err2
	}

	// Create the symlink
	memberSymlink := basePath + "/member/" + member.Url
	if err := os.Symlink(memberDir, memberSymlink); err != nil {
		return err
	}

	return nil
}

func (service *MemberService) Update(member model.Member) error {
	idPath := basePath + "/m/" + member.Id

	if err := service.RemoveSymlinkForId(member); err != nil {
		return err
	}

	// create new symlink
	newSymlink := basePath + "/member/" + member.Url
	if err := os.Symlink(idPath, newSymlink); err != nil {
		return err
	}

	return nil
}

func (service *MemberService) Archive(member model.Member) error {
	// remove symlink
	if err := service.RemoveSymlinkForId(member); err != nil {
		return err
	}

	// move directory to archived
	memberDir := basePath + "/m/" + member.Id
	archivedDir := basePath + "/archived/m/" + member.Id
	if err := os.Rename(memberDir, archivedDir); err != nil {
		return err
	}

	return nil
}

func (service *MemberService) RemoveSymlinkForId(member model.Member) error {
	idPath := basePath + "/m/" + member.Id

	// loop trough `basePath + "/member/"` look at all the symlink
	// and remove any of them that points to `idPath`
	urlDir := basePath + "/member"
	entries, err := os.ReadDir(urlDir)
	if err != nil {
		return err
	}
	for _, entry := range entries {
		if entry.Type()&os.ModeSymlink != 0 {
			symlinkPath := filepath.Join(urlDir, entry.Name())
			targetPath, err := os.Readlink(symlinkPath)
			if err != nil {
				// Handle error reading symlink target
				continue
			}
			if targetPath == idPath {
				err := os.Remove(symlinkPath)
				if err != nil {
					// Handle error removing symlink
					continue
				}
				fmt.Printf("Removed symlink %s pointing to %s\n", symlinkPath, targetPath)
			}
		}
	}
	return nil
}

func (service *MemberService) createFolderIfItDoesNotExist(urlDir string) error {
	_, err := os.ReadDir(urlDir)
	if err != nil {
		if err := os.Mkdir(urlDir, 0755); err != nil {
			return err
		}
	}
	return nil
}
