---
title: "video_format(7)"
name: "video_format"
section: "7"
letter: "v"
url: "/docs/linux/man/7-video_format/"
description: "video_format – Proposal For A Video Format Preference Specification"
---

<p>video_format &#8211; Proposal For A Video Format Preference Specification</p>
<h2>Description</h2>
<p>A number of different programs that create or work with video material need to know whether to generate their output in NTSC or PAL format. The ones that I’ve seen seem to have a hard-coded preference for one unless the user specifies the other. Overriding the default every time you want to use these programs gets tiresome. </p>
<p> Therefore, there needs to be a way for the user to configure a single default that will apply to all these programs. This default should be settable on a per-user basis and a systemwide basis, with the per-user setting overriding the systemwide one, as is usual. It makes sense to avoid dotfile clutter by following, at least to some extent, the XDG Base Directory Specification <a rel="nofollow" href="http://standards.freedesktop.org/basedir-spec/latest/.">http://standards.freedesktop.org/basedir-spec/latest/.</a> </p>
<p> The preference setting shall consist of the single word “NTSC” or “PAL” (without quotes, might as well be case-insensitive). This can be specified in the following ways, in order of decreasing priority:</p>
<dl>
<dt>&bull;</p>
<dd>As the value of the environment variable VIDEO_FORMAT</p>
<dt>&bull;</p>
<dd>As the contents of the user-specific file $XDG_CONFIG_HOME/video_format, with $XDG_CONFIG_HOME defaulting to $HOME/.config if not defined.</p>
<dt>&bull;</p>
<dd>As the contents of a systemwide file <i>dir</i>/video_format, where <i>dir</i> is taken in turn from the colon-separated items in the value of $XDG_CONFIG_DIRS until the file is found, or if $XDG_CONFIG_DIRS is not defined, then the single directory /etc.</dl>
<p> The application should use the first of these settings that it finds, searching in the specified order. </p>
<p> <code>Note:</code> the XDG Base Dir spec says systemwide config files should go in /etc/xdg. I&#8217;m not sure why this is, since lots of other apps put systemwide config in other places in /etc. Particularly since the spec doesn’t similarly restrict shared read-only data to just one subdirectory of /usr/share.</p>
<h2>Discussion</h2>
<p>Can this spec apply to both standard-definition and high-definition video? For standard definition, there is a difference of frame size, being 720 by 480 for NTSC and 720 by 576 for PAL (in both cases, the aspect ratio of the displayed image is always 4:3). But this doesn’t seem to matter for high definition. For both standard-definition and high-definition, there is a difference of frame rates, based around 29.97 fps for NTSC and 25 fps for PAL. </p>
<p> Note also that if a config file earlier in the search contains an invalid setting, the search does not continue even if another, later config file might contain a valid setting. This allows the user to override a system default with “no default”. Is this important? I think it could be.</p>
<h2>Reference Implementation</h2>
<p>The following Python code implements a routine called get_default_video_format that returns either one of the strings “NTSC” or “PAL” indicating the user/system-configured default format as per the spec above, or None if the default is invalid or not configured. </p>
<pre> class xdg_base_dir :
 &quot;Implementation of relevant parts of the XDG Base Directory specification&quot; \
 &quot; &lt;<a rel="nofollow" href="http://standards.freedesktop.org/basedir-spec/latest/">http://standards.freedesktop.org/basedir-spec/latest/</a>&gt;.&quot;
 @classmethod
 def get_config_home(self) :
 &quot;returns the directory for holding user-specific config files.&quot;
 result = os.environ.get(&quot;XDG_CONFIG_HOME&quot;)
 if result == None :
 result = os.path.join(os.environ[&quot;HOME&quot;], &quot;.config&quot;)
 #end if
 return result
 #end get_config_home
 @classmethod
 def config_search_path(self) :
 &quot;returns the list of config directories to search (apart from the user area).&quot;
 return tuple(os.environ.get(&quot;XDG_CONFIG_DIRS&quot;, &quot;/etc&quot;).split(&quot;:&quot;))
 # note spec actually says default should be /etc/xdg, but /etc is the
 # conventional location for system config files.
 #end config_search_path
 @classmethod
 def find_first_config_path(self, path) :
 &quot;searches for path in all the config directory locations in order of decreasing&quot; \
 &quot; priority, returning the expansion where it is first found, or None if not found.&quot;
 paths_to_try = iter((self.get_config_home(),) + self.config_search_path())
 # highest priority first
 while True :
 this_path = next(paths_to_try, None)
 if this_path == None :
 break
 this_path = os.path.join(this_path, path)
 if os.path.exists(this_path) :
 break
 #end while
 return this_path
 #end find_first_config_path
 #end xdg_base_dir
 valid_video_formats = frozenset((&quot;NTSC&quot;, &quot;PAL&quot;))
 def get_default_video_format() :
 video_format = os.environ.get(&quot;VIDEO_FORMAT&quot;)
 if video_format == None :
 config_file = xdg_base_dir.find_first_config_path(&quot;video_format&quot;)
 if config_file != None :
 try :
 video_format = open(config_file, &quot;r&quot;).readline().strip()
 except OSError :
 video_format = None
 #end try
 #end if
 #end if
 if video_format != None :
 video_format = video_format.upper()
 if video_format not in valid_video_formats :
 video_format = None
 #end if
 #end if
 return video_format
 #end get_default_video_format</pre>
