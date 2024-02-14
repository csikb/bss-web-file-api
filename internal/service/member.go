package service

import (
	"bssweb.bsstudio.hu/file-api/internal/model"
	"os"
)

func Create(member model.Member) error {
	// Create the member directory
	memberDir := "/data/member/" + member.Id
	if err := os.MkdirAll(memberDir, 0755); err != nil {
		return err
	}

	// Create the symlink
	memberSymlink := "/data/member/" + member.Url
	if err := os.Symlink(memberDir, memberSymlink); err != nil {
		return err
	}

	return nil
}

func Update(member model.Member) error {
	// remove symlink and create a new one
	// get old symlink by following the symlink
	oldSymlink, err := os.Readlink("/data/member/" + member.Id)

	if err == nil {
		return err
	}

	// remove old symlink
	if err := os.Remove(oldSymlink); err != nil {
		return err
	}

	// create new symlink
	newSymlink := "/data/member/" + member.Url
	if err := os.Symlink("/data/member/"+member.Id, newSymlink); err != nil {
		return err
	}

	return nil
}

func Archive(member model.Member) error {
	// remove symlink
	memberSymlink := "/data/member/" + member.Url
	if err := os.Remove(memberSymlink); err != nil {
		return err
	}

	// move directory to archived
	memberDir := "/data/member/" + member.Id
	archivedDir := "/data/archived/members" + member.Id
	if err := os.Rename(memberDir, archivedDir); err != nil {
		return err
	}

	return nil
}
