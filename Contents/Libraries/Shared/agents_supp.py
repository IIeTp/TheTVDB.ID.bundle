import os
from time import sleep

def check_agent(plugis_path, home_path):
  sleep(5)
# ############## Fanart.tv plugin
  # filepath = '%s/Fanart-TV.bundle/Contents/Code/%s' % (plugis_path, '__init__.py')
  # init_file = os.path.isfile(os.path.realpath(os.path.join(os.path.normpath(filepath))))
  # if init_file:
    # init_file = open(filepath,"r")
    # init_list = init_file.readlines()
    # try:
      # index_num = init_list.index("		'com.plexapp.agents.thetvdb',\n")
    # except:
      # index_num = None
    # init_file.close()
    # if index_num is not None:
      # init_list[index_num] = "		'com.plexapp.agents.thetvdb', 'com.plexapp.agents.thetvdb.id',\n"
      # index_num = init_list.index("		if media.primary_agent == 'com.plexapp.agents.thetvdb':\n")
      # init_list[index_num] = "		if media.primary_agent == 'com.plexapp.agents.thetvdb' or media.primary_agent == 'com.plexapp.agents.thetvdb.id':\n"      
      # init_file = open(filepath,"w")
      # for i in init_list:
         # init_file.write(i)
      # init_file.close()
# ################ OpenSubtitles plugin
  # filepath = '%s/OpenSubtitles.bundle/Contents/Code/%s' % (plugis_path, '__init__.py')
  # init_file = os.path.isfile(os.path.realpath(os.path.join(os.path.normpath(filepath))))
  # if init_file:
    # init_file = open(filepath,"r")
    # init_list = init_file.readlines()
    # try:
      # index_num = init_list.index("  contributes_to = ['com.plexapp.agents.thetvdb']\n")
    # except:
      # index_num = None
    # init_file.close()
    # if index_num is not None:
      # init_list[index_num] = "  contributes_to = ['com.plexapp.agents.thetvdb', 'com.plexapp.agents.thetvdb.id']\n"
      # init_file = open(filepath,"w")
      # for i in init_list:
         # init_file.write(i)
      # init_file.close()
# ############## PlexThemeMusic plugin
  # filepath = '%s/PlexThemeMusic.bundle/Contents/Code/%s' % (plugis_path, '__init__.py')
  # init_file = os.path.isfile(os.path.realpath(os.path.join(os.path.normpath(filepath))))
  # if init_file:
    # init_file = open(filepath,"r")
    # init_list = init_file.readlines()
    # try:
      # index_num = init_list.index("    'com.plexapp.agents.thetvdb',\n")
    # except:
      # index_num = None
    # init_file.close()
    # if index_num is not None:
      # init_list[index_num] = "    'com.plexapp.agents.thetvdb', 'com.plexapp.agents.thetvdb.id',\n"
      # index_num = init_list.index("    if media.primary_agent == 'com.plexapp.agents.thetvdb' or media.primary_agent == 'com.plexapp.agents.thetvdbdvdorder':\n")
      # init_list[index_num] = "    if media.primary_agent == 'com.plexapp.agents.thetvdb' or media.primary_agent == 'com.plexapp.agents.thetvdb.id' or media.primary_agent == 'com.plexapp.agents.thetvdbdvdorder':"
      # init_file = open(filepath,"w")
      # for i in init_list:
         # init_file.write(i)
      # init_file.close()