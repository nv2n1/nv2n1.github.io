---
title: "boom(5)"
name: "boom"
section: "5"
letter: "b"
url: "/docs/linux/man/5-boom/"
description: "boom.cfg, glboom.cfg – Configuration file for PrBoom v2.1.0 onwards"
---

<p>boom.cfg, glboom.cfg &#8211; Configuration file for PrBoom v2.1.0 onwards</p>
<h2>Usage</h2>
<p>When a version of PrBoom is run, it searches for this configuration file to modify its default settings. Every time PrBoom exits, it rewrites the configuration file, updating any settings that have been changed using the in-game menus. </p>
<p> PrBoom expects the config file to be <code>~/.prboom/boom.cfg</code>, or <code>~/.prboom/glboom.cfg</code> if compiled with GL support. Alternatively, it can be made to look elsewhere by using a command-line parameter: </p>
<p> {prboom,glboom} [<code>-config</code> <i>myconf</i>] .SH<code>FORMAT</code> <code>boom.cfg</code> consists of a number of variables and values. Each line is of the following format: </p>
<p> [ { &#123;&#123;#,;,[} <i>comment_text</i> , <i>variable </i> {<i>decimal_integer</i>, 0x&nbsp;<wbr><i>hex_integer</i>, &quot;<i>string_text</i>&quot;}}] </p>
<p> Any line beginning with a non-alphabetic character is treated as a comment and ignored; for future compatibility you should start comments with a <code>#</code>, <code>;</code> or <code>[</code>. Note however that when PrBoom rewrites boom.cfg it does not preserve user added comments. </p>
<p> Any line beginning with an alphabetic character is treated as a variable-value pair. The first word (sequence of non-whitespace characters) is the variable name, and everything after the following block of whitespace is taken to be the value assigned to the variable. </p>
<p> Variables not recognised by PrBoom, or which are given an invalid value or a value of an inappropriate type, are ignored. Warning messages are given where relevant. </p>
<p> The variables recognised by PrBoom are described per-section in the following sections. The sections are informal however; when PrBoom rewrites the config file it writes in section headings and puts variables into the relevant sections, but when reading these are ignored.</p>
<h2>Misc Settings</h2>
<dl>
<dt><code>compatibility_level</code></p>
<dd>PrBoom is capable of behaving in a way compatible with earlier versions of Doom and Boom/PrBoom. The value given here selects the version to be compatible with when doing new games/demos. See <code>README.compat</code> for details.</p>
<dt><code>realtic_clock_rate</code></p>
<dd>Selects the speed that PrBoom runs at, as a percentage of normal game speed. Leave at <code>0</code> unless you want to experiment. Note that it is considered `cheating&#8217; to use this at any setting below <code>0</code> (or above?).</p>
<dt><code>max_player_corpse</code></p>
<dd>Sets the maximum number of player corpses to leave lying around. If this limit would be exceeded, an old corpse is removed. Useful for big/long Deathmatch games, where the sheer number of corpses could slow the game down.</p>
<dt><code>flashing_hom</code></p>
<dd>Flag indicating whether a flashing red background is drawn to highlight HOM errors in levels (for level developers)</p>
<dt><code>demo_insurance</code></p>
<dd>Selects a method of protecting demos against `going out of sync&#8217; (where the player seems to lose control and behave madly, but in fact the players original instructions as stored in the demo have got out of sync with the game he was playing). <code>0</code>=No protection, <code>1</code>=Full protection, <code>2</code>=Only while recording demos. Safest when left set to <code>2</code>.</p>
<dt><code>endoom_mode</code></p>
<dd>This parameter specifies options controlling the display of the credits screen when Doom exits. Currently it is the sum of 3 options: add <code>1</code> for colours, <code>2</code> for non-ASCII characters to be displayed, and <code>4</code> for the last line to be skipped so the top line doesn&#8217;t scroll off screen.</p>
<dt><code>level_precache</code></p>
<dd>If set, when loading a new level PrBoom precaches all the graphics the level is likely to need in memory. This makes it much slower to load the level, but reduces disk activity and slowdowns reading data during play. Most systems are fast enough that precaching is not needed. </p>
</dl>
<h2>Files Settings</h2>
<dl>
<dt><code>wadfile_1, wadfile_2</code></p>
<dd>The names of 2 .wad files to be automatically loaded when PrBoom is started. A blank string means unused. </p>
<dt><code>dehfile_1, dehfile_2</code></p>
<dd>The names of 2 patch files (.deh or .bex) to be automatically loaded when PrBoom is started (empty string for none). </p>
</dl>
<h2>Game Settings</h2>
<dl>
<dt><code>default_skill</code></p>
<dd>The default skill level when starting a new game.</p>
<dt><code>weapon_recoil</code></p>
<dd>Enables recoil from weapon fire.</p>
<dt><code>doom_weapon_toggles</code></p>
<dd>Flag indicating whether pressing 3 or 1 when that weapon is already selected causes the selected shotgun or fist/chainsaw to be toggled, as in original Doom. Some people prefer to use a number for each weapon alone.</p>
<dt><code>player_bobbing</code></p>
<dd>Enables player bobbing (view randomly moving up/down slightly as the player runs).</p>
<dt><code>monsters_remember</code></p>
<dd>Makes monsters remember their previous enemy after killing their current target.</p>
<dt><code>monster_infighting</code></p>
<dd>Whether monsters will fight each other when they injure each other accidentally.</p>
<dt><code>monster_backing</code></p>
<dd>Whether monsters without close combat weapons will back away from close combat (unlike original Doom).</p>
<dt><code>monster_avoid_hazards</code></p>
<dd>Whether monsters avoid crushing ceilings.</p>
<dt><code>monkeys</code></p>
<dd>Whether monsters will climb steep stairs.</p>
<dt><code>monster_friction</code></p>
<dd>Whether monsters are affected by changed floor friction (they should be, but weren&#8217;t in Boom)</p>
<dt><code>help_friends</code></p>
<dd>Whether monsters will help out injured monsters by aiding them against their attacker.</p>
<dt><code>player_helpers</code></p>
<dd>The number of helper dogs to spawn.</p>
<dt><code>friend_distance</code></p>
<dd>Distance within which friends will generally stay.</p>
<dt><code>dog_jumping</code></p>
<dd>Whether dogs will jump.</p>
<dt><code>sts_always_red</code></p>
<dd>PrBoom can make the colour of the text displays on the status bar reflect your current status (<code>red</code>=low, <code>yellow</code>=average, <code>green</code>=good, <code>blue</code>=super-charged). This option if set selects the traditional Doom behavior of always-red status bar display; set to <code>0</code> to allow the coloured display.</p>
<dt><code>sts_pct_always_gray</code></p>
<dd>See above, this makes just the percent signs always gray, instead of changing colour.</p>
<dt><code>sts_traditional_keys</code></p>
<dd>Doom and PrBoom have two types of keys; PrBoom will normally display both keys of a given colour if you have both. This option, if enabled, instead makes PrBoom only ever display one key of each colour, in the same way Doom did.</p>
<dt><code>traditional_menu</code></p>
<dd>Changes PrBoom&#8217;s menu ordering to be the same as original Doom if enabled.</p>
<dt><code>show_messages</code></p>
<dd>When enabled, text messages are displayed in the top left corner of the screen describing events in the game. Can be toggled in the game, this is just to preserve the setting.</p>
<dt><code>autorun</code></p>
<dd>Makes the player always run, without having to hold down a run key. Can be toggled in the game, this just preserves the setting. </p>
</dl>
<h2>Sound Settings</h2>
<dl>
<dt><code>sound_card</code></p>
<dd>Selects whether sound effects are enabled (non-zero enables). For compatibility reasons with Boom, a range of values are accepted.</p>
<dt><code>music_card</code></p>
<dd>Selects whether in-game music is enabled (non-zero enables). For compatibility reasons a range of values are accepted.</p>
<dt><code>pitched_sounds</code></p>
<dd>If enabled by this variable, this enables `pitching&#8217; (making pitch adjustments to the playing sounds) for 16 bit sound cards.</p>
<dt><code>samplerate</code></p>
<dd>The samplerate for soundmixing and timidity. The sound quality is much better at higher samplerates, but if you use timidity then higher samplerates need much more CPU power. Useful values are <code>11025</code>, <code>22050</code>, <code>44100</code> and <code>48000</code>.</p>
<dt><code>sfx_volume</code></p>
<dd>Sound effects volume. This is best adjusted in the game.</p>
<dt><code>music_volume</code></p>
<dd>Music volume. This is best adjusted in the game.</p>
<dt><code>mus_pause_opt</code></p>
<dd>Selects what PrBoom does to the music when a games is paused. <code>0</code>=stop the music, <code>1</code>=pause the music (stop it playing, but when resumed resume it at the same place &#8211; not implemented), <code>2</code>=continue playing.</p>
<dt><code>sounddev</code>,&nbsp;<wbr><code>snd_channels</code>,&nbsp;<wbr><code>soundsrv</code>,&nbsp;<wbr><code>musicsrv</code></p>
<dd>These variables are no longer used by PrBoom, but are kept for compatibility reasons. </p>
</dl>
<h2>Compatibility Settings</h2>
<p>These are settings that let you choose whether the normal game mechanics are used, or whether various quirks, bugs and limitations of the original Doom game are emulated.</p>
<h2>Video Settings</h2>
<dl>
<dt><code>screen_width</code>,&nbsp;<wbr><code>screen_height</code></p>
<dd>For versions of PrBoom which support high-res, these specify the default screen or window size for PrBoom. These settings are ignored and preserved by versions of PrBoom which do not do high-res (they assume 320&#215;200).</p>
<dt><code>use_fullscreen</code></p>
<dd>If set, this causes PrBoom to try to go full screen. Depending on your video driver and mode, this may include changing screen resolution to better match the game&#8217;s screen resolution.</p>
<dt><code>use_doublebuffer</code></p>
<dd>Use double buffering to reduce tearing. On some machines this is even faster than the normal method, but on others this makes problems, so you have to try out which setting works best.</p>
<dt><code>translucency</code></p>
<dd>Causes PrBoom to display certain objects as translucent.</p>
<dt><code>tran_filter_pct</code></p>
<dd>Selects how translucent objects are when they are translucent. Play with this and see for yourself.</p>
<dt><code>screenblocks</code></p>
<dd>Selects a reduced screen size inside the PrBoom window (the player&#8217;s view is surrounded by a border). Normally this is undesirable, but it can help speed up the game. Can be changed in the game with the +/- keys, this variable is just to preserve that setting.</p>
<dt><code>usegamma</code></p>
<dd>Selects a level of gamma correction (extra screen brightening) to correct for a dark monitor or light surroundings. Can be selected in the game with the F11 key, this config entry preserves that setting. </p>
</dl>
<h2>Opengl Settings</h2>
<p>If you are knowledgeable about OpenGL, you can tweak various aspects of the GL rendering engine.</p>
<dl>
<dt><code>gl_nearclip</code></p>
<dd>The near clipping plane *100.</p>
<dt><code>gl_colorbuffer_bits</code></p>
<dd>The bit depth for the framebuffer. (<code>16</code>, <code>24</code> or <code>32</code> bits)</p>
<dt><code>gl_depthbuffer_bits</code></p>
<dd>The bit depth for the z-buffer. (<code>16</code>, <code>24</code> or <code>32</code> bits)</p>
<dt><code>gl_tex_filter_string</code></p>
<dd>A string, one of the following: <code>GL_NEAREST</code> or <code>GL_LINEAR</code> (no mipmapping), or one of <code>GL_NEAREST_MIPMAP_NEAREST</code>, <code>GL_NEAREST_MIPMAP_LINEAR</code>, <code>GL_LINEAR_MIPMAP_NEAREST</code>, <code>GL_LINEAR_MIPMAP_LINEAR</code> with mipmapping.</p>
<dt><code>gl_tex_format_string</code></p>
<dd>One of the following strings: <code>GL_RGBA</code> &#8211; means format selected by driver (not so good), <code>GL_RGBA2</code> &#8211; means 2 bits for each component (bad), <code>GL_RGBA4</code> &#8211; means 4 bits for each component (like <code>GL_RGBA</code> on most cards), <code>GL_RGB5_A1</code> &#8211; means 5 bits for each color component 1 bit for the alpha channel (default), <code>GL_RGBA8</code> &#8211; means 8 bits for each component (best quality, but only a little bit better than <code>GL_RGB5_A1</code> and slower on most cards)</p>
<dt><code>gl_drawskys</code></p>
<dd>If <code>0</code>, disables drawing skies, which may be needed with some problematic 3D cards.</p>
<dt><code>gl_sortsprites</code></p>
<dd>Experimental option, possibly faster but less reliable. </p>
</dl>
<h2>Mouse Settings</h2>
<p>This section specifies settings for using a mouse with PrBoom. There are several settings that control button bindings (what action each button causes in the game); these are easiest set from the in-game menus, these config entries are to preserve the settings between games.</p>
<dl>
<dt><code>use_mouse</code></p>
<dd>Enable or disable the use of a mouse with PrBoom.</p>
<dt><code>mouse_sensitivity_horiz</code>,&nbsp;<wbr><code>mouse_sensitivity_vert</code></p>
<dd>Sets the sensitivity of the mouse in PrBoom. Easier set from the in-game menus. </p>
</dl>
<h2>Key Bindings</h2>
<p>These specify the keys that trigger various actions in PrBoom. The codes used for keys are internal to PrBoom, though many keys are represented by their ASCII codes. It is easiest to modify these via the in-game menus (OPTIONS-&gt;SETUP-&gt;KEY BINDINGS). These config file entries preserve the settings from this menu between game sessions.</p>
<h2>Joystick Settings</h2>
<p>There are the trigger variables here, which are calculated during joystick calibration (the values received from the kernel driver outside of which movement is caused in the game). Also there are the button-bindings, again best adjusted using the in-game menus.</p>
<dl>
<dt><code>use_joystick</code></p>
<dd>This selects the number of the joystick to use, or <code>0</code> selects no joystick. You have to have the relevant device files (<code>/dev/js0</code> etc) and the kernel driver loaded. </p>
</dl>
<h2>Chat Macros</h2>
<p>These are pre-written text strings for quick transmission to players in a network game (consult your Doom documentation). Easiest set via the in-game menus (OPTIONS-&gt;SETUP-&gt;CHAT MACROS).</p>
<h2>Automap Settings</h2>
<p>These are settings related to the automap. These are easiest set from within the game.</p>
<h2>Heads_Up Display Settings</h2>
<p>These are settings related to the heads-up display, that is messages received while playing and the heads-up display of your current status obtained by pressing + while the view is full-screen in PrBoom. See the Boom documentation for details. All controlled best from within the game.</p>
<h2>Weapon Preferences</h2>
<p>Here are the settings from the Weapons menu in the game (OPTIONS-&gt;SETUP-&gt;WEAPONS).</p>
<h2>Also See</h2>
<p><code><a href="/docs/linux/man/6-prboom/">prboom</a>(6),</code> PrBoom&#8217;s documentation (including the Boom and MBF documentation) and your Doom documentation.</p>
<h2>Author</h2>
<p>See the file <code>AUTHORS</code> included with PrBoom for a list of contributors to PrBoom. This config file reference written by Colin Phipps (cph [at] moria.org.uk).</p>
