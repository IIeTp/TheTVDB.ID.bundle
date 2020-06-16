# TheTVDB.ID
This agent is based on the original **TheTVDB** plugin. For the improvement of the code, thanks go to [Reyter](https://github.com/ReyterAK).

The main differences from the original version:
- Added the ability to use the ID from TV show, instead of the name or in addition to it.
- Added the ability to use ID from [FileBot Xattr Metadata](https://github.com/filebot/plex-agents), for support, installation of this plugin is required.

## Examples
[Arrow](https://thetvdb.com/series/arrow) tvdb-ID = 257655
It does not matter what the name of the file is, if tvdb-ID is specified in the filepath, then the information will be bound to the ID.
Pattern: tvdb-00000 

* `\tvdb-257655\s01e01.mkv` = `Arrow (2012) - s01e01 - Pilot`                                   
* `\we\like\what\TVDB-257655\we\do\s01e01.m2ts` = `Arrow (2012) - s01e01 - Pilot`
* `\s01e01 tvdb257655.mp4` = `Arrow (2012) - s01e01 - Pilot`                           
Note: standard plex scanners ignore the BDMV folder, so if you store movies in the BDAV/BDMV folder structure, you will have to use a third-party scanner, for example [FileBot Xattr Metadata](https://github.com/filebot/plex-agents) *(this scanner can only work with xattr metadata)*.

## Install
1. Download [TheTVDB.ID.bundle](https://github.com/IIeTp/TheTVDB.ID.bundle/archive/master.zip)
2. Move TheTVDB.ID.bundle to the default plugins folder. [FAQ](https://support.plex.tv/articles/202915258-where-is-the-plex-media-server-data-directory-located/)            
   `%LOCALAPPDATA%\Plex Media Server\Plug-ins` for Windows Vista/7/8/10
