---
title: "xlock(1)"
name: "xlock"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xlock/"
description: "xlock – Locks the local X display until a password is entered."
---

<h2>NAME</h2>
<p> xlock &#8211; Locks the local X display until a password is entered. </p>
<h2>SYNOPSIS</h2>
<p> <code>xlock</code> [ <code>-help</code> ] [ <code>-version</code> ] [ <code>-resources</code> ] [ <code>-display</code><i> displayname</i> ] [ <code>-visual</code><i> visualname</i> ] [ <code>-name</code><i> resourcename</i> ] [ <code>-mode</code><i> modename</i> ] [ <code>-delay</code><i> usecs</i> ] [ <code>-batchcount</code><i> num</i> ] [ <code>-count</code><i> num</i> ] [ <code>-cycles</code><i> num</i> ] [ <code>-ncolors</code><i> num</i> ] [ <code>-size</code><i> num</i> ] [ <code>-saturation</code><i> value</i> ] [ <code>-erasemode</code><i> modename</i> ] [ <code>-erasedelay</code><i> usecs</i> ] [ <code>-/+allowaccess</code> ] [ <code>-vtlock</code><i> modename</i> ] [ <code>-/+nolock</code> ] [ <code>-/+inwindow</code> ] [ <code>-/+inroot</code> ] [ <code>-/+remote</code> ] [ <code>-/+mono</code> ] [ <code>-/+allowroot</code> ] [ <code>-/+debug</code> ] [ <code>-/+description</code> ] [ <code>-/+echokeys</code> ] [ <code>-echokey</code><i> echokey</i> ] [ <code>-/+enablesaver</code> ] [ <code>-/+resetsaver</code> ] [ <code>-/+grabmouse</code> ] [ <code>-/+grabserver</code> ] [ <code>-/+install</code> ] [ <code>-/+mousemotion</code> ] [ <code>-/+sound</code> ] [ <code>-/+showdate</code> ] [ <code>-/+timeelapsed</code> ] [ <code>-/+usefirst</code> ] [ <code>-/+verbose</code> ] [ <code>-nice</code><i> level</i> ] [ <code>-lockdelay</code><i> seconds</i> ] [ <code>-timeout</code><i> seconds</i> ] [ <code>-font</code><i> fontname</i> ] [ <code>-planfont</code><i> fontname</i> ] [ <code>-bg</code><i> color</i> ] [ <code>-fg</code><i> color</i> ] [ <code>-background</code><i> color</i> ] [ <code>-foreground</code><i> color</i> ] [ <code>-username</code><i> string</i> ] [ <code>-password</code><i> string</i> ] [ <code>-info</code><i> string</i> ] [ <code>-validate</code><i> string</i> ] [ <code>-invalid</code><i> string</i> ] [ <code>-geometry</code><i> geom</i> ] [ <code>-icongeometry</code><i> geom</i> ] [ <code>-glgeometry</code><i> geom</i> ] [ <code>-/+wireframe</code> ] [ <code>-/+showfps</code> ] [ <code>-fpsfont</code><i> fontname</i> ] [ <code>-/+fpstop</code> ] [ <code>-/+use3d</code> ] [ <code>-delta3d</code><i> value</i> ] [ <code>-none3d</code><i> color</i> ] [ <code>-right3d</code><i> color</i> ] [ <code>-left3d</code><i> color</i> ] [ <code>-both3d</code><i> color</i> ] [ <code>-program</code><i> programname</i> ] [ <code>-messagesfile</code><i> formatted-filename</i> ] [ <code>-messagefile</code><i> filename</i> ] [ <code>-message</code><i> string</i> ] [ <code>-messagefont</code><i> fontname</i> ] [ <code>-bitmap</code><i> filename</i> ] [ <code>-cpasswd</code><i> crypted-password</i> ] [ <code>-forceLogout</code><i> minutes</i> ] [ <code>-logoutButton</code><i> minutes</i> ] [ <code>-logoutButtonLabel</code><i> textstring</i> ] [ <code>-logoutButtonHelp</code><i> textstring</i> ] [ <code>-logoutFailedString</code><i> textstring</i> ] [ <code>-/+dtsaver</code> ] [ <code>-/+xinerama</code> ] [ <code>-modulepath</code><i> path</i> ] [ <code>-locksound</code><i> string</i> ] [ <code>-infosound</code><i> string</i> ] [ <code>-validsound</code><i> string</i> ] [ <code>-invalidsound</code><i> string</i> ] [ <code>-startCmd</code><i> string</i> ] [ <code>-endCmd</code><i> string</i> ] [ <code>-pipepassCmd</code><i> string</i> ] [ <code>-logoutCmd</code><i> string</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>xlock</code> locks the X server till the user enters their password at the keyboard. While <code>xlock</code> is running, all new server connections are refused. The screen saver is disabled. The mouse cursor is turned off. The screen is blanked and a changing pattern is put on the screen. If a key or a mouse button is pressed then the user is prompted for the password of the user who started <code>xlock</code>. </p>
<p> If the correct password is typed, then the screen is unlocked and the X server is restored. When typing the password Control-U and Control-H are active as kill and erase respectively. To return to the locked screen, click in the small icon version of the changing pattern. </p>
<p> In the lower part of the password screen a text is displayed. This message is taken from the first file of the following that exists: $HOME/.xlocktext, $HOME/.plan, or $HOME/.signature. </p>
<p> On systems which support new BSD style authentication, the password may be prefixed by an authentication style followed by a colon (i.e. &quot;style:password&quot;). See the <a href="/docs/linux/man/5-login-conf/">login.conf</a>(5) for more information on authentication styles. </p>
<h2>NOTE ON ETIQUETTE</h2>
<p> <i>Xlock</i> should not be used on public terminals when there is a high demand for them. </p>
<p> If you find a public terminal that has been locked by another user and there are no other terminals available, and the terminal appears to have been left idle for a while (normally more than 15 minutes), it is fair to try to reset the session in some manner. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-help</code></p>
<dd> Print options and a brief description to standard output.</p>
<dt><code>-version</code></p>
<dd> Print version number (if &gt;= 4.00) to standard output.</p>
<dt><code>-resources</code></p>
<dd> Print default resource file to standard output.</p>
<dt><code>-display</code><i>&nbsp;<wbr>displayname</i></p>
<dd> The <i>display</i> option sets the X11 display to lock. <code>xlock</code> locks all available screens on a given server, and restricts you to locking only a local server such as <code>unix:0,</code> <code>localhost:0,</code> or <code>:0</code> unless you set the <code>-remote</code> option.</p>
<dt><code>-visual</code><i>&nbsp;<wbr>visualname</i></p>
<dd> <i>visualname</i> which is one of &quot;StaticGray&quot;, &quot;GrayScale&quot;, &quot;StaticColor&quot;, &quot;PseudoColor&quot;, &quot;TrueColor&quot;, &quot;DirectColor&quot;, or &quot;default&quot;. default used to set the screen&#8217;s default visual (the visual of the root window).</p>
<dt><code>-name</code><i>&nbsp;<wbr>resourcename</i></p>
<dd> <i>resourcename</i> is used instead of <code>XLock</code> when looking for resources to configure <code>xlock</code>.</p>
<dt><code>-mode</code><i>&nbsp;<wbr>modename</i></p>
<dd> As of this writing there are over 90 display modes supported (plus one more for random selection of one of these).</p>
<dt><code>anemone</code></p>
<dd> Shows wiggling tentacles.</p>
<dt><code>ant</code></p>
<dd> Shows Langton&#8217;s and Turk&#8217;s generalized ants.</p>
<dt><code>ant3d</code></p>
<dd> Shows 3D ants.</p>
<dt><code>apollonian</code></p>
<dd> Shows Apollonian circles.</p>
<dt><code>atlantis</code></p>
<dd> Shows moving sharks/whales/dolphin. May not be available depending on how it was configured.</p>
<dt><code>atunnels</code></p>
<dd> Advance GL tunnels screensaver. May not be available depending on how it was configured.</p>
<dt><code>ball</code></p>
<dd> Shows bouncing balls.</p>
<dt><code>bat</code></p>
<dd> Shows bouncing flying bats.</p>
<dt><code>blot</code></p>
<dd> Shows Rorschach&#8217;s ink blot test.</p>
<dt><code>bouboule</code></p>
<dd> Shows Mimi&#8217;s bouboule of moving stars.</p>
<dt><code>bounce</code></p>
<dd> Shows bouncing footballs.</p>
<dt><code>braid</code></p>
<dd> Shows random braids and knots.</p>
<dt><code>bubble</code></p>
<dd> Shows popping bubbles.</p>
<dt><code>bubble3d</code></p>
<dd> Shows Richard Jones&#8217;s GL bubbles. May not be available depending on how it was configured.</p>
<dt><code>bug</code></p>
<dd> Shows Palmiter&#8217;s bug evolution and a garden of Eden.</p>
<dt><code>clock</code></p>
<dd> Shows Packard&#8217;s oclock.</p>
<dt><code>coral</code></p>
<dd> Shows a coral reef.</p>
<dt><code>crystal</code></p>
<dd> Shows polygons in 2D plane groups.</p>
<dt><code>daisy</code></p>
<dd> Shows a meadow of daisies.</p>
<dt><code>dclock</code></p>
<dd> Shows a floating digital clock or message.</p>
<dt><code>deco</code></p>
<dd> Shows art as ugly as sin.</p>
<dt><code>demon</code></p>
<dd> Shows Griffeath&#8217;s cellular automata.</p>
<dt><code>dilemma</code></p>
<dd> Shows Lloyd&#8217;s Prisoner&#8217;s Dilemma simulation.</p>
<dt><code>discrete</code></p>
<dd> Shows various discrete maps.</p>
<dt><code>dragon</code></p>
<dd> Shows Deventer&#8217;s Hexagonal Dragons Maze.</p>
<dt><code>drift</code></p>
<dd> Shows cosmic drifting flame fractals.</p>
<dt><code>cage</code></p>
<dd> Shows the Impossible Cage, an Escher-like GL scene. May not be available depending on how it was configured.</p>
<dt><code>euler2d</code></p>
<dd> Shows a simulation of 2D incompressible inviscid fluid.</p>
<dt><code>eyes</code></p>
<dd> Shows eyes following a bouncing grelb.</p>
<dt><code>fadeplot</code></p>
<dd> Shows a fading plot of sine squared.</p>
<dt><code>fiberlamp</code></p>
<dd> Shows a Fiber Optic Lamp.</p>
<dt><code>fire</code></p>
<dd> Shows a 3D fire-like image. May not be available depending on how it was configured.</p>
<dt><code>flag</code></p>
<dd> Shows a waving flag image. This may be text or a graphic image. Default text is the hostname and operating system.</p>
<dt><code>flame</code></p>
<dd> Shows cosmic flame fractals.</p>
<dt><code>flow</code></p>
<dd> Shows dynamic strange attractors.</p>
<dt><code>forest</code></p>
<dd> Shows binary trees of a fractal forest.</p>
<dt><code>fzort</code></p>
<dd> Shows a metallic-looking fzort.</p>
<dt><code>galaxy</code></p>
<dd> Shows crashing spiral galaxies.</p>
<dt><code>gears</code></p>
<dd> Shows GL&#8217;s gears. May not be available depending on how it was configured.</p>
<dt><code>glplanet</code></p>
<dd> Animates texture mapped sphere (planet)</p>
<dt><code>goop</code></p>
<dd> Shows goop from a lava lamp.</p>
<dt><code>grav</code></p>
<dd> Shows orbiting planets.</p>
<dt><code>helix</code></p>
<dd> Shows string art.</p>
<dt><code>hop</code></p>
<dd> Shows real plane iterated fractals.</p>
<dt><code>hyper</code></p>
<dd> Shows spinning n-dimensional hypercubes.</p>
<dt><code>ico</code></p>
<dd> Shows a bouncing polyhedron.</p>
<dt><code>ifs</code></p>
<dd> Shows a modified iterated function system.</p>
<dt><code>image</code></p>
<dd> Shows randomly appearing logos.</p>
<dt><code>juggle</code></p>
<dd> Shows a Juggler, juggling.</p>
<dt><code>juggle</code></p>
<dd> Shows a 3D Juggler, juggling.</p>
<dt><code>julia</code></p>
<dd> Shows the Julia set.</p>
<dt><code>kaleid</code></p>
<dd> Shows Brewster&#8217;s Kaleidoscope.</p>
<dt><code>kumppa</code></p>
<dd> Shows kumppa.</p>
<dt><code>laser</code></p>
<dd> Shows spinning lasers.</p>
<dt><code>life</code></p>
<dd> Shows Conway&#8217;s game of life.</p>
<dt><code>life1d</code></p>
<dd> Shows Wolfram&#8217;s game of 1D life.</p>
<dt><code>life3d</code></p>
<dd> Shows Bays&#8217; game of 3D life.</p>
<dt><code>lightning</code></p>
<dd> Shows Keith&#8217;s fractal lightning bolts.</p>
<dt><code>lisa</code></p>
<dd> Shows animated lissajous loops.</p>
<dt><code>lissie</code></p>
<dd> Shows lissajous worms.</p>
<dt><code>loop</code></p>
<dd> Shows Langton&#8217;s self-producing loops.</p>
<dt><code>mandelbrot</code></p>
<dd> Shows mandelbrot sets.</p>
<dt><code>marquee</code></p>
<dd> Shows text.</p>
<dt><code>matrix</code></p>
<dd> Shows the matrix.</p>
<dt><code>maze</code></p>
<dd> Shows a random maze and a depth first search solution.</p>
<dt><code>moebius</code></p>
<dd> Shows the Moebius Strip II, an Escher-like GL scene with ants. May not be available depending on how it was configured.</p>
<dt><code>molecule</code></p>
<dd> Draws molecules, based on coordinates from PDB (Protein Data Base) files.</p>
<dt><code>morph3d</code></p>
<dd> Shows GL morphing polyhedra. May not be available depending on how it was configured.</p>
<dt><code>mountain</code></p>
<dd> Shows Papo&#8217;s mountain range.</p>
<dt><code>munch</code></p>
<dd> Shows munching squares.</p>
<dt><code>noof</code></p>
<dd> Shows SGI Diatoms.</p>
<dt><code>nose</code></p>
<dd> Shows a man with a big nose runs around spewing out text.</p>
<dt><code>pacman</code></p>
<dd> Shows Pacman(tm).</p>
<dt><code>penrose</code></p>
<dd> Shows Penrose&#8217;s quasiperiodic tilings.</p>
<dt><code>petal</code></p>
<dd> Shows various GCD Flowers.</p>
<dt><code>petri</code></p>
<dd> Shows a mold simultation in a petri dish</p>
<dt><code>pipes</code></p>
<dd> Shows a self-building pipe system. May not be available depending on how it was configured.</p>
<dt><code>polyominoes</code></p>
<dd> Shows attempts to place polyominoes into a rectangle.</p>
<dt><code>puzzle</code></p>
<dd> Shows a puzzle being scrambled and then solved.</p>
<dt><code>pyro</code></p>
<dd> Shows fireworks.</p>
<dt><code>pyro2</code></p>
<dd> Shows other fireworks.</p>
<dt><code>qix</code></p>
<dd> Shows spinning lines a la Qix(tm).</p>
<dt><code>roll</code></p>
<dd> Shows a rolling ball.</p>
<dt><code>rain</code></p>
<dd> Shows rain.</p>
<dt><code>rotor</code></p>
<dd> Shows Tom&#8217;s Roto-Rooter.</p>
<dt><code>rubik</code></p>
<dd> Shows an auto-solving Rubik&#8217;s Cube. May not be available depending on how it was configured.</p>
<dt><code>sballs</code></p>
<dd> Shows balls spinning like crazy in GL. May not be available depending on how it was configured.</p>
<dt><code>scooter</code></p>
<dd> Shows a journey through space tunnel and stars.</p>
<dt><code>shape</code></p>
<dd> Shows stippled rectangles, ellipses, and triangles.</p>
<dt><code>sierpinski</code></p>
<dd> Shows a Sierpinski&#8217;s triangle.</p>
<dt><code>sierpinski3d</code></p>
<dd> Shows a Sierpinski&#8217;s gasket.</p>
<dt><code>skewb</code></p>
<dd> Shows an auto-solving Skewb. May not be available depending on how it was configured.</p>
<dt><code>slip</code></p>
<dd> Shows slipping blits.</p>
<dt><code>solitaire</code></p>
<dd> Shows Klondike&#8217;s game of solitaire.</p>
<dt><code>space</code></p>
<dd> Shows a journey into deep space.</p>
<dt><code>sphere</code></p>
<dd> Shows a bunch of shaded spheres.</p>
<dt><code>spiral</code></p>
<dd> Shows a helical locus of points.</p>
<dt><code>spline</code></p>
<dd> Shows colorful moving splines.</p>
<dt><code>sproingies</code></p>
<dd> Shows Sproingies! Nontoxic. Safe for pets and small children. May not be available depending on how it was configured.</p>
<dt><code>stairs</code></p>
<dd> Shows Infinite Stairs, an Escher-like GL scene. May not be available depending on how it was configured.</p>
<dt><code>star</code></p>
<dd> Shows a star field with a twist.</p>
<dt><code>starfish</code></p>
<dd> Shows starfish.</p>
<dt><code>strange</code></p>
<dd> Shows strange attractors.</p>
<dt><code>superquadrics</code></p>
<dd> Shows 3D mathematical shapes. May not be available depending on how it was configured.</p>
<dt><code>swarm</code></p>
<dd> Shows a swarm of bees following a wasp.</p>
<dt><code>swirl</code></p>
<dd> Shows animated swirling patterns.</p>
<dt><code>t3d</code></p>
<dd> Shows a Flying Balls Clock Demo.</p>
<dt><code>tetris</code></p>
<dd> Shows an autoplaying tetris game.</p>
<dt><code>text3d | text3d2</code></p>
<dd> Shows 3D moving texts.</p>
<dt><code>thornbird</code></p>
<dd> Shows an animated Bird in a Thorn Bush fractal map.</p>
<dt><code>tik_tak</code></p>
<dd> Shows rotating polygons.</p>
<dt><code>toneclock</code></p>
<dd> Shows Peter Schat&#8217;s toneclock.</p>
<dt><code>triangle</code></p>
<dd> Shows a triangular mountain range.</p>
<dt><code>tube</code></p>
<dd> Shows an animated tube.</p>
<dt><code>turtle</code></p>
<dd> Shows turtle fractals.</p>
<dt><code>vines</code></p>
<dd> Shows fractal-like vines.</p>
<dt><code>voters</code></p>
<dd> Shows Dewdney&#8217;s Voters.</p>
<dt><code>wator</code></p>
<dd> Shows Dewdney&#8217;s Water-Torus planet of fish and sharks.</p>
<dt><code>wire</code></p>
<dd> Shows a random circuit with 2 electrons.</p>
<dt><code>world</code></p>
<dd> Shows spinning Earths.</p>
<dt><code>worm</code></p>
<dd> Shows wiggly worms.</p>
<dt><code>xjack</code></p>
<dd> Shows Jack having one of those days.</p>
<dt><code>xcl</code></p>
<dd> Shows a Control Line combat model race</p>
<dt><code>blank</code></p>
<dd> Shows nothing but a black screen. Does not show up in random mode.</p>
<dt><code>bomb</code></p>
<dd> Shows a bomb and will autologout after a time. Does not show up in random mode and may be available depending on how it was configured.</p>
<dt><code>random</code></p>
<dd> Shows a random mode from above except blank (and bomb). </p>
<dt><code>-delay</code><i>&nbsp;<wbr>usecs</i></p>
<dd> The <i>delay</i> option sets the speed at which a mode will operate. It simply sets the number of microseconds to delay between batches of animations. In blank mode, it is important to set this to some small number of seconds, because the keyboard and mouse are only checked after each delay, so you cannot set the delay too high, but a delay of zero would needlessly consume cpu checking for mouse and keyboard input in a tight loop, since blank mode has no work to do.</p>
<dt><code>-count</code><i>&nbsp;<wbr>num</i></p>
<dd> The <i>batchcount</i> option sets number of <i>things</i> to do per batch to <i>num .</i> </p>
<p> In anenome mode it is means nothing. </p>
<p> In ant and ant3d modes this refers the number of ants. </p>
<p> In apollonian mode it is the number of possible ways to imbed circles within a circle, all of integer curvature. </p>
<p> In atlantis mode it is the number of sharks. </p>
<p> In atunnels mode it is means nothing. </p>
<p> In ball mode it is the number of balls. </p>
<p> In bat mode it is the number of bats, could be less because of conflicts. </p>
<p> In blot mode this refers to the number of pixels rendered in the same color. </p>
<p> In bouboule mode it is the number of stars. </p>
<p> In bounce mode it is the number of balls, could be less because of conflicts. </p>
<p> In braid mode it is the upper bound number of strands. </p>
<p> In bubble mode it is the number of bubbles. </p>
<p> In bubble3d mode it is the number of bubbles. </p>
<p> In bug mode it is the number of bugs, could be less because of conflicts. </p>
<p> In cage mode it is means nothing. </p>
<p> In clock mode it is the percentage of the screen, but less than 100%. </p>
<p> In coral mode it is the number of seeds. </p>
<p> In crystal mode it is the number of polygons. </p>
<p> In daisy mode it is the number flowers that make a meadow. </p>
<p> In dclock mode it means nothing. </p>
<p> In deco mode it is the depth. </p>
<p> In demon mode this refers the number of colors. </p>
<p> In dilemma mode this refers the number of initial defectors. </p>
<p> In discrete mode it is the number of points. </p>
<p> In drift mode it is the number of levels to recurse (larger = more complex). </p>
<p> In dragon mode it means nothing. </p>
<p> In euler2d mode it is the number of segments. </p>
<p> In eyes mode it is the number of eyes. </p>
<p> In fadeplot mode it is the number of steps. </p>
<p> In fiberlamp it is the number of fibers. </p>
<p> In fire mode it is the number of fire particles (set it to 0 to have rain). </p>
<p> In flag mode it means nothing. </p>
<p> In flame mode it is the number of levels to recurse (larger = more complex). </p>
<p> In flow mode it is the number of bees. </p>
<p> In forest mode it is the number trees that make a forest. </p>
<p> In fzort mode it means nothing. </p>
<p> In galaxy mode it means the number of galaxies. </p>
<p> In gears mode it is the number of degrees to rotate the set of gears by. </p>
<p> In glplanet mode it is the number of hundredth degrees to roll the planet by. </p>
<p> In goop mode it is the number of blobs per plane. </p>
<p> In grav mode it is the number of planets. </p>
<p> In helix mode it means nothing. </p>
<p> In hop mode this refers to the number of pixels rendered in the same color. </p>
<p> In hyper mode it the number of dimensions. </p>
<p> In ico mode it is the ith platonic solid. </p>
<p> In ifs mode it means nothing. </p>
<p> In image mode it means it is the number of logos on screen at once. </p>
<p> In juggle mode it is time in milliseconds between a throw and the next catch. </p>
<p> In juggler3d mode it is time in milliseconds between a throw and the next catch. </p>
<p> In julia mode it is the depth of recursion. </p>
<p> In kaleid mode it is the number of pens. </p>
<p> In kumppa mode it means nothing. </p>
<p> In lament mode it means nothing. </p>
<p> In laser mode it is the number lasers. </p>
<p> In life and life3d modes it is the number of generations before a glider is introduced. </p>
<p> In life1d mode it means nothing. </p>
<p> In lisa mode it is the number of loops. </p>
<p> In lissie mode it is the number of worms. </p>
<p> In loop mode it is the number of flaws. </p>
<p> In mandelbrot mode it is the order. </p>
<p> In marquee mode it means nothing. </p>
<p> In matrix mode it means nothing. </p>
<p> In maze mode it means nothing. </p>
<p> In moebius mode it is means nothing. </p>
<p> In molecule mode it means nothing. </p>
<p> In morph3d mode it is the ith platonic solid. </p>
<p> In mountain mode it is the number of mountains. </p>
<p> In munch mode it means nothing. </p>
<p> In noof mode it means nothing. </p>
<p> In nose mode it means nothing. </p>
<p> In qix mode it is the number of points. </p>
<p> In pacman mode it means the number of ghosts. </p>
<p> In penrose mode it means nothing. </p>
<p> In petal mode it the greatest random number of petals. </p>
<p> In petri mode it means nothing. </p>
<p> In pipes mode it shows different joints, 0 random, 1 spherical, 2 bolted elbow, 3 elbow, and 4 alternating. </p>
<p> In polyominoes mode it means nothing. </p>
<p> In puzzle mode it the number of moves. </p>
<p> In pyro mode it is the maximum number flying rockets at one time. </p>
<p> In pyro2 mode it is means nothing. </p>
<p> In rain mode it is means nothing. </p>
<p> In roll mode it is the number of points. </p>
<p> In rotor mode it is the number of rotor thingys which whirr&#8230; </p>
<p> In rubik mode it is the number of moves. </p>
<p> In sballs mode it is the number of spheres. </p>
<p> In scooter mode it is the number of doors. </p>
<p> In shape mode it means nothing. </p>
<p> In sierpinski mode it is the number of points. </p>
<p> In skewb mode it is the number of moves. </p>
<p> In slip mode it means nothing. </p>
<p> In solitaire mode it means nothing. </p>
<p> In space mode it is the number of stars. </p>
<p> In sphere mode it means nothing. </p>
<p> In spiral mode it is the number of spirals. </p>
<p> In spline mode it is the number of points &quot;splined&quot;. </p>
<p> In sproingies mode it is the number of sproingies. </p>
<p> In stairs mode it is means nothing. </p>
<p> In star mode it is the number of stars on the screen at once. </p>
<p> In starfish mode it means nothing. </p>
<p> In strange mode it means nothing. </p>
<p> In superquadrics mode its the number of horizontal and vertical lines in the superquadric. </p>
<p> In swirl mode it means the number of &quot;knots&quot;. </p>
<p> In swarm mode it is the number of bees. </p>
<p> In t3d mode it means nothing. </p>
<p> In tetris mode it means nothing. </p>
<p> In text3d mode it means nothing. </p>
<p> In thornbird mode it is the number of points. </p>
<p> In triangular mode it is the number of mountains. </p>
<p> In tube mode it is a rectangle (= 1), an ellipse (= 2), or a polygon if greater. </p>
<p> In turtle mode it means nothing. </p>
<p> In vines mode it is draw a complete vine (= 0) or a portion (= 1). </p>
<p> In voters mode it means the number of parties, 2 or 3. </p>
<p> In wator mode it means the breed time for the fish. </p>
<p> In wire mode it means the length of the circuit. </p>
<p> In world mode it is the number of worlds. </p>
<p> In worm mode it is the number of worms. </p>
<p> In xcl mode it represents the number of planes. </p>
<p> In xjack mode it means nothing. </p>
<p> In blank mode it means nothing. </p>
<p> In bomb mode it means the number of minutes to autologout. </p>
<p> A negative <i>count</i> allows for randomness. The range from the minimum allowed nonnegative <i>count</i> for a particular mode to the ABS( <i>count</i> ) (or maximum allowed <i>count</i> , whichever is less).</p>
<dt><code>-batchcount</code><i>&nbsp;<wbr>num</i></p>
<dd> The <i>batchcount</i> option is deprecated but should still work as <i>count.</i></p>
<dt><code>-cycles</code><i>&nbsp;<wbr>num</i></p>
<dd> The <i>cycles</i> option sets the number of cycles until time out for ant, ant3d, apollonian, blot, braid, bug, clock, crystal, daisy, deco, demon, dilemma, discrete, dragon, eyes, fiberlamp, flag, flow, forest, galaxy, helix, hop, hyper, ico, juggle, juggler3d, laser, life, life1d, life3d, lisa, lissie, loop, mandelbrot, mountain, petal, sierpinski, shape, spline +erase, t3d, thornbird, triangle, tube, voters, wator, and wire. For euler2d and worm it is the length of the lines, for atlantis it is the shark speed, for fadeplot, julia and spiral it is the length of the trail of dots, munch it is the minimum size of the squares, for kaleid it is the % of black, for qix it is the number of lines, for spline -erase it means the number of splines * 64 (for compatibility with +erase), for gears it is the number of degrees to increment the spin of each gear by, for glplanet it is the number of hundredth degrees to rotate the planet by, for molecule it is the time in seconds until timeout, for pipes it is the number of systems to draw before clearing the screen, for rubik it is the number of steps to complete a 90 degree move, for sballs it is the sphere speed value, for scooter it is the speed, for skewb it is the number of steps to complete a 120 degree move, for superquadrics it is the number of frames it takes to morph from one shape to another. for text3d it is the number of times drawing a word before the next one, For others it means nothing.</p>
<dt><code>-size</code><i>&nbsp;<wbr>num</i></p>
<dd> The <i>size</i> option sets the size maximum size of a star in bouboule, pyro and star, size of ball in ball and bounce, size of bat in bat, maximum size of bubble in bubble, size of clock in clock, minimum size of rectangles in deco, size of the polygons in crystal, tik_tak, and toneclock, size of polyhedron in ico, size of lissie in lissie, size of dots of flag, for kaleid it is the symmetry, width of maze hallway, size of side of penrose tile, radius of loop in lisa, radius of ball in roll, number of corners in sierpinski, number of stars in scooter, size of tube in tube, width of worm in worm, line width in rotor, size of cells in ant, bug, dilemma, dragon, life, life1d, pacman, petri, tetris, voters, wator, and wire. In pipes it is the maximum length of a system. In flow and swarm it is the length of the lines. In atlantis it is the shark size. A negative number allows for randomness, similar to <i>count.</i> In atunnels, fire, gears, sballs and sproingies it is the size of the screen (default 400), this is because on many slow systems it runs too slow when the picture covers the full screen. Set to 0 for full screen on fast machines.</p>
<dt><code>-ncolors</code><i>&nbsp;<wbr>num</i></p>
<dd> The <i>ncolors</i> option sets the maximum number of colors to be used.</p>
<dt><code>-saturation</code><i>&nbsp;<wbr>value</i></p>
<dd> The <i>saturation</i> option sets saturation of the color ramp used to <i>value .</i> 0 is grayscale and 1 is very rich color. 0.4 is a nice pastel.</p>
<dt><code>-erasemode</code><i>&nbsp;<wbr>modename</i></p>
<dd> As of this writing there are over 12 erase modes supported (if its not chosen its assumed random). The erase modes are random_lines, random_squares, venetian, triple_wipe, quad_wipe, circle_wipe, three_circle_wipe, squaretate, fizzle, spiral, slide_lines, losira, no_fade. <i>modename</i> is now similar to the option <code>modelist</code> where you can it can be something like &quot;all-losira&quot; to get all erasemodes but losira. Use a &quot;+&quot; or a &quot;,&quot; to add modes like &quot;spiral+venetian&quot;.</p>
<dt><code>-erasedelay</code><i>&nbsp;<wbr>usecs</i></p>
<dd> The <i>erasedelay</i> option sets the number of microseconds for steps of the <code>erasemode</code> (a setting of 0 and the <code>erasemode</code> is bypassed).</p>
<dt><code>+/-nolock</code></p>
<dd> The <i>nolock</i> option causes <code>xlock</code> to only draw the patterns and not lock the display. A key press or a mouse click will terminate the screen saver.</p>
<dt><code>-/+inwindow</code></p>
<dd> Runs <code>xlock</code> in a window, so that you can iconify, move, or resize it and still use your screen for other stuff. When running in a window, <code>xlock</code> no longer locks your screen, it just looks good.</p>
<dt><code>-/+inroot</code></p>
<dd> Runs <code>xlock</code> in your root window. Like the <i>inwindow</i> option it no longer locks the screen, it just looks good.</p>
<dt><code>-/+remote</code></p>
<dd> The <i>remote</i> option tells <code>xlock</code> to not stop you from locking remote X11 servers. This option should be used with care and is intended mainly to lock X11 terminals which cannot run <code>xlock</code> locally. If you lock someone else&#8217;s workstation, they will have to know <code>your</code> password to unlock it. Using <i>+remote</i> overrides any resource derived values for <i>remote</i> and prevents <code>xlock</code> from being used to lock other X11 servers. (Use `+&#8217; instead of `-&#8216; to override resources for other options that can take the `+&#8217; modifier similarly.)</p>
<dt><code>-/+mono</code></p>
<dd> The <i>mono</i> option causes <code>xlock</code> to display monochrome, (black and white) pixels rather than the default colored ones on color displays.</p>
<dt><code>-/+allowaccess</code></p>
<dd> This option is required for servers which do not allow clients to modify the host access control list. It is also useful if you need to run x clients on a server which is locked for some reason&#8230; When <i>allowaccess</i> is true, the X11 server is left open for clients to attach and thus lowers the inherent security of this lock screen. A side effect of using this option is that if <code>xlock</code> is killed -KILL, the access control list is not lost.</p>
<dt><code>-vtlock</code><i>&nbsp;<wbr>modename</i></p>
<dd> This option is used on a XFree86 system to manage VT switching in [off|noswitch|switch|restore] mode.</p>
<dt><i>off</i></p>
<dd> means no VT switch locking.</p>
<dt><i>switch</i></p>
<dd> means VT switch locking + switching to xlock VT when activated.</p>
<dt><i>restore</i></p>
<dd> means VT switch locking + switching to xlock VT when activated + switching back to previous VT when desactivated.</p>
<dt><i>noswitch</i></p>
<dd> means VT switch locking only when xlock VT is active.</p>
<dt><code>-/+allowroot</code></p>
<dd> The <i>allowroot</i> option allows the root password to unlock the server as well as the user who started <code>xlock</code>. May not be able to turn this on and off depending on your system and how <code>xlock</code> was configured.</p>
<dt><code>-/+debug</code></p>
<dd> Allows <code>xlock</code> to be debugged by doing all but locking the screen.</p>
<dt><code>-/+description</code></p>
<dd> The <i>description</i> option causes <code>xlock</code> shows a mode description above password window. The default is to show this description.</p>
<dt><code>-/+echokeys</code></p>
<dd> The <i>echokeys</i> option causes <code>xlock</code> to echo &#8216;?&#8217; characters (default) for each key typed into the password prompt. Some consider this a security risk, so the default is to not echo anything.</p>
<dt><code>-echokey</code><i>&nbsp;<wbr>echokey</i></p>
<dd> The text character to use for echo key in <i>echokeys .</i></p>
<dt><code>-/+enablesaver</code></p>
<dd> By default <code>xlock</code> will disable the normal X server&#8217;s screen saver since it is in effect a replacement for it. Since it is possible to set delay parameters long enough to cause phosphor burn on some displays, this option will turn back on the default screen saver which is very careful to keep most of the screen black.</p>
<dt><code>-/+resetsaver</code></p>
<dd> By default <code>xlock</code> will call XResetScreenSaver. This may be undesirable with DPMS monitors.</p>
<dt><code>-/+grabmouse</code></p>
<dd> The <i>grabmouse</i> option causes <code>xlock</code> to grab the mouse and keyboard, this is the default. <code>xlock</code> can not lock the screen without this.</p>
<dt><code>-/+grabserver</code></p>
<dd> The <i>grabserver</i> option causes <code>xlock</code> to grab the server. This is not usually needed but some unsecure X servers can be defeated without this.</p>
<dt><code>-/+install</code></p>
<dd> Allows <code>xlock</code> to install its own colormap if <code>xlock</code> runs out of colors. May not work on with some window managers (fvwm) and does not work with the -inroot option.</p>
<dt><code>-/+mousemotion</code></p>
<dd> Allows you to turn on and off the sensitivity to the mouse to bring up the password window.</p>
<dt><code>-/+sound</code></p>
<dd> Allows you to turn on and off sound if installed with the capability.</p>
<dt><code>-/+showdate</code></p>
<dd> Allows you to turn on and off the date on password window. On by default.</p>
<dt><code>-/+timeelapsed</code></p>
<dd> Allows you to find out how long a machine is locked so you can complain to an administrator that someone is hogging a machine.</p>
<dt><code>-/+usefirst</code></p>
<dd> The <i>usefirst</i> option causes <code>xlock</code> to use the keystroke which got you to the password screen as the first character in the password. The default is to ignore the first key pressed.</p>
<dt><code>-/+verbose</code></p>
<dd> Verbose mode, tells what options it is going to use.</p>
<dt><code>-nice</code><i>&nbsp;<wbr>nicelevel</i></p>
<dd> The <i>nice</i> option sets system nicelevel of the <code>xlock</code> process to <i>nicelevel .</i></p>
<dt><code>-lockdelay</code><i>&nbsp;<wbr>seconds</i></p>
<dd> The <i>lockdelay</i> option sets the number of <i>seconds</i> before the screen needs a password to be unlocked. Good for use with an autolocking mechanism like <a href="/docs/linux/man/1-xautolock/">xautolock</a>(1).</p>
<dt><code>-timeout</code><i>&nbsp;<wbr>seconds</i></p>
<dd> The <i>timeout</i> option sets the number of <i>seconds</i> before the password screen will time out.</p>
<dt><code>-font</code><i>&nbsp;<wbr>fontname</i></p>
<dd> The <i>font</i> option sets the font to be used on the prompt screen.</p>
<dt><code>-planfont</code><i>&nbsp;<wbr>fontname</i></p>
<dd> option sets the font to be used for the text that is displayed in the lower part of the password screen.</p>
<dt><code>-fg</code><i>&nbsp;<wbr>color</i></p>
<dd> The <i>fg</i> option sets the color of the text on the password screen to <i>color .</i></p>
<dt><code>-bg</code><i>&nbsp;<wbr>color</i></p>
<dd> The <i>bg</i> option sets the color of the background on the password screen to <i>color .</i></p>
<dt><code>-foreground</code><i>&nbsp;<wbr>color</i></p>
<dd> The <i>foreground</i> option sets the color of the text on the password screen to <i>color .</i></p>
<dt><code>-background</code><i>&nbsp;<wbr>color</i></p>
<dd> The <i>background</i> option sets the color of the background on the password screen to <i>color .</i></p>
<dt><code>-username</code><i>&nbsp;<wbr>string</i></p>
<dd> Text <i>string</i> is shown in front of user name, defaults to &quot;Name: &quot;.</p>
<dt><code>-password</code><i>&nbsp;<wbr>string</i></p>
<dd> Text <i>string</i> is the password prompt string, defaults to &quot;Password: &quot;.</p>
<dt><code>-info</code><i>&nbsp;<wbr>string</i></p>
<dd> Text <i>string</i> is an informational message to tell the user what to do, defaults to &quot;Enter password to unlock; select icon to lock.&quot;.</p>
<dt><code>-validate</code><i>&nbsp;<wbr>string</i></p>
<dd> Text <i>string</i> is a message shown while validating the password, defaults to &quot;Validating login&#8230;&quot;</p>
<dt><code>-invalid</code><i>&nbsp;<wbr>string</i></p>
<dd> Text <i>string</i> is a message shown when password is invalid, defaults to &quot;Invalid login.&quot;</p>
<dt><code>-geometry</code><i>&nbsp;<wbr>geom</i></p>
<dd> The <i>geometry</i> option sets <i>geom</i> the size and offset of the lock window (normally the entire screen). The entire screen format is still used for entering the password. The purpose is to see the screen even though it is locked. This should be used with caution since many of the modes will fail if the windows are far from square or are too small (size must be greater than 0x0). This should also be used with -enablesaver to protect screen from phosphor burn.</p>
<dt><code>-icongeometry</code><i>&nbsp;<wbr>geom</i></p>
<dd> The <i>icongeometry</i> option sets <i>geom</i> the size of the iconic screen (normally 64&#215;64) seen when entering the password. This should be used with caution since many of the modes will fail if the windows are far from square or are too small (size must be greater than 0x0). The greatest size is 256&#215;256. There should be some limit so users could see who has locked the screen. Position information of icon is ignored.</p>
<dt><code>-glgeometry</code><i>&nbsp;<wbr>geom</i></p>
<dd> The <i>glgeometry</i> option sets <i>geom</i> the size of the screen for gl modes. Not normally available or needed.</p>
<dt><code>-/+wireframe</code></p>
<dd> Turn on/off wireframe, available on ant3d, atlantis, atunnels, daisy, fire, gears, lament, life3d, mountain, sballs, sproingies, superquadrics, and triangle.</p>
<dt><code>-/+showfps</code></p>
<dd> Turn on/off frame per sec display, available on atlantis, atunnels, bubble3d, cage, fire, gears, invert, lament, moebius, morph3d, rubik, sballs, skewb, stairs, and superquadrics.</p>
<dt><code>-/+fpstop</code></p>
<dd> Turn on/off frame per sec display on top of screen, used if showfps is on.</p>
<dt><code>-fpsfont</code><i>&nbsp;<wbr>fontname</i></p>
<dd> The <i>fpsfont</i> option sets the font to be used in the frame per sec display, used if showfps is on.</p>
<dt><code>-/+use3d</code></p>
<dd> Turn on/off 3d view, available on bouboule, pyro, star, and worm.</p>
<dt><code>-delta3d</code><i>&nbsp;<wbr>value</i></p>
<dd> Space between the center of your 2 eyes for 3d mode.</p>
<dt><code>-none3d</code><i>&nbsp;<wbr>color</i></p>
<dd> Color used for empty size in 3d mode.</p>
<dt><code>-right3d</code><i>&nbsp;<wbr>color</i></p>
<dd> Color used for right eye in 3d mode.</p>
<dt><code>-left3d</code><i>&nbsp;<wbr>color</i></p>
<dd> Color used for left eye in 3d mode.</p>
<dt><code>-both3d</code><i>&nbsp;<wbr>color</i></p>
<dd> Color used for overlapping images for left and right eye in 3d mode.</p>
<dt><code>-program</code><i>&nbsp;<wbr>programname</i></p>
<dd> The <i>program</i> option sets the program to be used as the fortune generator. Currently used only for marquee and nose modes.</p>
<dt><code>-messagesfile</code><i>&nbsp;<wbr>formatted-filename</i></p>
<dd> The <i>messagesfile</i> option sets the file to be used as the fortune generator. The first entry is the number of fortunes, the next line contains the first fortune. Fortunes begin with a &quot;%%&quot; on a line by itself. Currently used only for marquee and nose modes. If one exists, it takes precedence over the fortune program.</p>
<dt><code>-messagefile</code><i>&nbsp;<wbr>filename</i></p>
<dd> The <i>messagefile</i> option sets the file whose contents are displayed. Currently used only for marquee and nose modes. If one exists, it takes precedence over the fortune program and messagesfile.</p>
<dt><code>-message</code><i>&nbsp;<wbr>textstring</i></p>
<dd> The <i>message</i> option sets the text to be displayed in a mode. Currently used only for flag, marquee and nose modes. If one exists, it takes precedence over the fortune program, messagesfile and message.</p>
<dt><code>-messagefont</code><i>&nbsp;<wbr>fontname</i></p>
<dd> The <i>messagefont</i> option sets the font to be used in the mode. Currently used only for flag, marquee, and nose modes.</p>
<dt><code>-bitmap</code><i>&nbsp;<wbr>filename</i></p>
<dd> The <i>bitmap</i> option sets the xbm, xpm, or ras file to be displayed with flag, image, life, life1d, maze, or puzzle mode. For eyes and pacman only a xbm file is accepted. Certain modes reject the bitmap if too big. / </p>
</dl>
<h2>MORE OPTIONS (these may not be available)</h2>
<dl>
<dt><code>-cpasswd</code><i>&nbsp;<wbr>crypted-password</i></p>
<dd> The <i>cpasswd</i> option sets the key to be this text string to unlock <code>xlock</code> instead of password file.</p>
<dt><code>-forceLogout</code><i>&nbsp;<wbr>minutes</i></p>
<dd> The <i>forceLogout</i> option sets <i>minutes</i> to auto-logout.</p>
<dt><code>-logoutButton</code><i>&nbsp;<wbr>minutes</i></p>
<dd> The <i>logoutButton</i> option sets <i>minutes</i> to logoutButton is available on password screen.</p>
<dt><code>-logoutButtonLabel</code><i>&nbsp;<wbr>string</i></p>
<dd> Text <i>string</i> is a message shown inside logout button when logout button is displayed. Defaults to &quot;Logout&quot;.</p>
<dt><code>-logoutButtonHelp</code><i>&nbsp;<wbr>string</i></p>
<dd> Text <i>string</i> is a message shown outside logout button when logout button is displayed. Defaults to &quot;Click the \&quot;Logout\&quot; button to log out current
 user and make workstation available.&quot;</p>
<dt><code>-logoutFailedString</code><i>&nbsp;<wbr>string</i></p>
<dd> Text <i>string</i> is a message shown when a logout is attempted and fails. Defaults to &quot;Logout attempt FAILED.
 Current user could not be automatically logged out.&quot;</p>
<dt><code>-/+dtsaver</code></p>
<dd> Turn on/off CDE Saver Mode. This option is only available if CDE support was compiled in.</p>
<dt><code>-/+xinerama</code></p>
<dd> Turn on/off Xinerama. This option is only available if Xinerama support was compiled in.</p>
<dt><code>-modulepath</code><i>&nbsp;<wbr>path</i></p>
<dd> The <i>modulepath</i> option sets the <i>directories</i> that <code>xlock</code> searches for mode modules to load. It is a colon separated list of directories to search. If &quot;%S&quot; is included in the path, it is replaced by the default modulepath. To add a private module directory to the default path, use something like &#8216;%S:~/mymoduledir&#8217; as the path. This option is only available if module support was compiled in.</p>
<dt><code>-locksound</code><i>&nbsp;<wbr>string</i></p>
<dd> Text <i>string</i> references sound to use at lock time. Default sound, male voice: &quot;Thank you, for your cooperation.&quot;</p>
<dt><code>-infosound</code><i>&nbsp;<wbr>string</i></p>
<dd> Text <i>string</i> references sound to use for information. Default sound, male voice: &quot;Identify please.&quot;</p>
<dt><code>-validsound</code><i>&nbsp;<wbr>string</i></p>
<dd> Text <i>string</i> references sound to when a password is valid. Default sound, female voice: &quot;Complete.&quot;</p>
<dt><code>-invalidsound</code><i>&nbsp;<wbr>string</i></p>
<dd> Text <i>string</i> references sound to when a password is invalid. Default sound, female voice: &quot;I am not programmed to give you that information.&quot;</p>
<dt><code>-startCmd</code><i>&nbsp;<wbr>string</i></p>
<dd> Text <i>string</i> command to execute when the screen is locked. Commonly used instructions include: &quot;zaway&quot;. This command, if still running when the screensaver exits, will be killed.</p>
<dt><code>-endCmd</code><i>&nbsp;<wbr>string</i></p>
<dd> Text <i>string</i> command to execute when the screen is unlocked.</p>
<dt><code>-pipepassCmd</code><i>&nbsp;<wbr>string</i></p>
<dd> Text <i>string</i> command into which to pipe the password when the screen is unlocked.</p>
<dt><code>-logoutCmd</code><i>&nbsp;<wbr>string</i></p>
<dd> Text <i>string</i> command to execute when the program logs the user out (either via the autologout or by pressing the logout button).</p>
<dt><code>-mailCmd</code><i>&nbsp;<wbr>string</i></p>
<dd> Text <i>string</i> command to execute when the program to check mail.</p>
<dt><code>-mailIcon</code><i>&nbsp;<wbr>string</i></p>
<dd> Text <i>string</i> of file for the &quot;mail arrived&quot; bitmap.</p>
<dt><code>-nomailIcon</code><i>&nbsp;<wbr>string</i></p>
<dd> Text <i>string</i> of file for the &quot;no mail&quot; bitmap.</p>
<dt><code>-dpmsstandby &nbsp;<wbr>seconds</code></p>
<dd> Allows one to set DPMS Standby for monitor (0 is defined as infinite). (Horizontal sync on, Vertical sync off, RGB guns off, power supply on, tube filaments energized, (screen saver mode). Typical 17 inch screen&#8230; 110 out of 120 watts with a 3 sec recovery time.) This option is only available if DPMS support was compiled in. Minimum timeout is 5 seconds.</p>
<dt><code>-dpmssuspend &nbsp;<wbr>seconds</code></p>
<dd> Allows one to set DPMS Suspend for monitor (0 is defined as infinite). (Horizontal sync off, Vertical sync on, RGB guns off, power supply off, tube filaments energized. Typical 17 inch screen &#8230; 15 out of 120 watts with a 3 sec recovery time.) This option is only available if DPMS support was compiled in. Minimum timeout is 5 seconds.</p>
<dt><code>-dpmsoff &nbsp;<wbr>seconds</code></p>
<dd> Allows one to set DPMS Power Off for monitor (0 is defined as infinite). (Horizontal sync off, Vertical sync off, Small auxiliary circuit stays on to monitor the HS/VS signals to enable power on when data needs to be displayed on the screen. Typical 17 inch screen &#8230; 5 out of 120 watts with a 10 sec recovery time.) This option is only available if DPMS support was compiled in. Minimum timeout is 5 seconds. </p>
</dl>
<h2>SPECIAL MODE DEPENDENT OPTIONS</h2>
<dl>
<dt><code>-neighbors</code><i>&nbsp;<wbr>num</i></p>
<dd> The <i>neighbors</i> option sets the number of neighbors of a cell to 3, 4, 6, 9 (may not have real mathematical meaning), or 12 for several automata modes <i>(ant, bug, demon, dilemma, life, loop, voters, wator,</i> and <i>wire) (bug</i> and <i>loop</i> do not span this full range). Setting it to 0 typically randomizes this, except where bitmaps are used <i>(dilemma, life, voters,</i> and <i>wator).</i></p>
<dt><code>-/+eyes</code></p>
<dd> Turn on and off eyes for <i>ant, ant3d,</i> and <i>bug.</i></p>
<dt><code>-/+cycle</code></p>
<dd> Turn on and off colour cycling in <i>crystal, lyapunov, mandelbrot, starfish, swirl, tetris, tik_tak, toneclock,</i> and <i>tube.</i></p>
<dt><code>-/+label</code></p>
<dd> Turn on and off alternate space and number labeling in <i>apollonian.</i> For <i>ant</i> and <i>ant3d</i> this turns on and off the labeling of the rule. For <i>life</i> and <i>life3d</i> this turns on and off the labeling of the pattern name and rule.</p>
<dt><code>-/+serial</code></p>
<dd> Turn on and off sequential allocation of colors in <i>kaleid.</i> For <i>life</i> and <i>life3d</i> this turns on and off the picking of sequential patterns (to be used with middle button of the mouse).</p>
<dt><code>-/+trackmouse</code></p>
<dd> Turn on and off mouse interaction in <i>eyes, fire, julia, solitaire, sballs, swarm,</i> and <i>tetris.</i> For <i>maze, pacman, solitaire</i> and <i>tetris</i> this may not be available depending on how <code>xlock</code> was configured.</p>
<dt><code>-/+texture</code></p>
<dd> Turn on and off texturing in <i>fire,</i> <i>lament</i> and <i>sballs.</i> This may not be available depending on how <code>xlock</code> was configured.</p>
<dt><code>-rule</code><i>&nbsp;<wbr>&lt;rule&gt;</i></p>
<dd> The rule string is defined as S&lt;neighborhood&gt;/B&lt;neighborhood&gt; for <i>life</i> and <i>life3d.</i> Special parameters: P, picks a random rule from all rules that have known patterns; G, picks a random rule from all rules that have known gliders. For <i>life</i> a good example is Conway&#8217;s rule which is S23/B3. Others are B36/S23 and B3678/S34678. For <i>life3d</i> good examples are Bay&#8217;s rules which are S45/B5, S567/B6, S56/B5, and S67/B67. The rule string is defined as a binary string (requires at least one 1 and one 0) for <i>ant</i> and a base 4 (or quadranary) string (requires 3 of 4 digits to be represented) for <i>ant3d.</i> Here a special parameter, T and then a number, will pick a specific table.</p>
<dt><code>-lifefile</code><i>&nbsp;<wbr>filename</i></p>
<dd> The <i>lifefile</i> option sets the <i>life</i> and <i>life3d</i> lifeform. Only one format is currently supported, similar to the #P xlife format. For <i>life3d,</i> 2 linefeeds in a row are assumed to advance the depth.</p>
<dt><code>-arms</code><i>&nbsp;<wbr>num</i></p>
<dd> Allows one to set the number of arms in <i>anemone.</i></p>
<dt><code>-finpoints</code><i>&nbsp;<wbr>num</i></p>
<dd> Allows one to set the width of the arms in <i>anemone.</i></p>
<dt><code>-width</code><i>&nbsp;<wbr>num</i></p>
<dd> Allows one to set the final number of points in each array of <i>anemone.</i></p>
<dt><code>-withdraws</code><i>&nbsp;<wbr>num</i></p>
<dd> Allows one to set the withdraw frequency in</p>
<dt><i>anemone.</i></p>
<dd> <code>-turnspeed</code><i>&nbsp;<wbr>num</i> Allows one to set the turning speed in</p>
<dt><code>-/+truchet</code></p>
<dd> Turn on and off Truchet lines (trail) in <i>ant.</i></p>
<dt><code>-/+altgeom</code></p>
<dd> Turn on and off alternate geometries (off euclidean space, on includes spherical and hyperbolic) in <i>apollonian</i> mode.</p>
<dt><code>-whalespeed</code><i>&nbsp;<wbr>num</i></p>
<dd> Allows one to set the speed of the whales and dolphin in <i>atlantis.</i></p>
<dt><code>-/+boil</code></p>
<dd> Turn on and off having the bubbles bubble up in <i>bubble.</i></p>
<dt><code>-nx</code><i>&nbsp;<wbr>num</i></p>
<dd> Allows one to set the number of unit cells in x-direction in <i>crystal.</i></p>
<dt><code>-ny</code><i>&nbsp;<wbr>num</i></p>
<dd> Allows one to set the number of unit cells in y-direction in <i>crystal.</i></p>
<dt><code>-/+centre</code></p>
<dd> Turn on and off the centering on screen in <i>crystal.</i></p>
<dt><code>-/+maxsize</code></p>
<dd> Turn on and off the centering on screen in <i>crystal.</i></p>
<dt><code>-/+cell</code></p>
<dd> Turn on and off the drawing of unit cell in <i>crystal.</i></p>
<dt><code>-/+grid</code></p>
<dd> Turn on and off the drwing of grid of unit cells (if -cell is on) in <i>crystal.</i></p>
<dt><code>-/+garden</code></p>
<dd> Turn off and on garden look in <i>daisy.</i></p>
<dt><code>-/+binary</code></p>
<dd> Turn on and off the binary clock in <i>dclock.</i></p>
<dt><code>-/+led</code></p>
<dd> Turn on and off the led clock in <i>dclock.</i></p>
<dt><code>-/+popex</code></p>
<dd> Turn on and off the population explosion counter in <i>dclock.</i></p>
<dt><code>-/+forest</code></p>
<dd> Turn on and off the tropical deforest (hectares/acres) counter in <i>dclock.</i></p>
<dt><code>-/+hiv</code></p>
<dd> Turn on and off the HIV infection counter in <i>dclock.</i></p>
<dt><code>-/+lab</code></p>
<dd> Turn on and off the Animal Research counter in <i>dclock.</i></p>
<dt><code>-/+veg</code></p>
<dd> Turn on and off the Animal Consumation counter in <i>dclock.</i></p>
<dt><code>-/+y2k</code></p>
<dd> Turn on and off the Year 2000 countdown in <i>dclock.</i></p>
<dt><code>-/+millennium</code></p>
<dd> Turn on and off the Second Millennium (January 1, 2001) countdown in <i>dclock.</i></p>
<dt><code>-bonus</code><i>&nbsp;<wbr>value</i></p>
<dd> Allows one to set the bonus for cheating&#8230; between 1.0 and 4.0 in <i>dilemma.</i></p>
<dt><code>-/+conscious</code></p>
<dd> Turn off and on self-awareness in <i>dilemma.</i></p>
<dt><code>-/+grow</code></p>
<dd> Turn on and off growing fractals (else they are animated) for <i>drift.</i></p>
<dt><code>-/+liss</code></p>
<dd> Turn on and off using lissajous figures to get points for <i>drift.</i></p>
<dt><code>-/+fog</code></p>
<dd> Turn on and off fog for <i>fire.</i></p>
<dt><code>-/+shadows</code></p>
<dd> Turn on and off shadows for <i>fire.</i></p>
<dt><code>-trees</code><i>&nbsp;<wbr>num</i></p>
<dd> Validate the displaying of trees for <i>fire</i> if greater than zero.</p>
<dt><code>-/+invert</code></p>
<dd> Turn on and off inverting of the <i>flag.</i></p>
<dt><code>-/+rotate</code></p>
<dd> Turn on/off rotating around attractor in <i>flow.</i></p>
<dt><code>-/+ride</code></p>
<dd> Turn on/off rideing in the <i>flow.</i></p>
<dt><code>-/+box</code></p>
<dd> Turn on/off bounding box in <i>flow.</i></p>
<dt><code>-/+periodic</code></p>
<dd> Turn on/off periodic attractors in <i>flow.</i></p>
<dt><code>-/+search</code></p>
<dd> Turn on/off search for new attractors in <i>flow.</i></p>
<dt><code>-/+dbuf</code></p>
<dd> Turn on/off double buffering in <i>flow.</i></p>
<dt><code>-/+tracks</code></p>
<dd> Turn on and off star tracks in <i>galaxy.</i></p>
<dt><code>-/+light</code></p>
<dd> Turn on and off lighting of the planet for <i>glplanet.</i></p>
<dt><code>-/+bounce</code></p>
<dd> Turn on and off bouncing movement of the planet for <i>glplanet.</i></p>
<dt><code>-pimage</code><i>&nbsp;<wbr>filename</i></p>
<dd> Use the named xbm or xpm file for texturing the planet for <i>glplanet.</i> Use BUILTIN as filename for the builtin image taken from Xearth.</p>
<dt><code>-/+roll</code></p>
<dd> Turn on and off rolling of the planet for <i>glplanet.</i></p>
<dt><code>-/+rotate</code></p>
<dd> Turn on and off rotation of the planet for <i>glplanet.</i></p>
<dt><code>-/+texture</code></p>
<dd> Turn on and off texturing of the planet for <i>glplanet.</i></p>
<dt><code>-/+stars</code></p>
<dd> Turn on and off showing stars in the background for <i>glplanet.</i></p>
<dt><code>-/+decay</code></p>
<dd> Turn on and off decaying orbits for <i>grav.</i></p>
<dt><code>-/+trail</code></p>
<dd> Turn on and off decaying trail of dots for <i>grav.</i></p>
<dt><code>-/+ellipse</code></p>
<dd> Turn on and off ellipse format in <i>helix.</i></p>
<dt><code>-/+martin</code></p>
<dd> Turn on and off Barry Martin&#8217;s square root <i>hop.</i> <code>-/+popcorn</code> Turn on and off Clifford A. Pickover&#8217;s popcorn <i>hop.</i></p>
<dt><code>-/+ejk1&#8230;ejk6</code></p>
<dd> Turn on and off Ed J. Kubaitis&#8217; <i>hops.</i></p>
<dt><code>-/+rr</code></p>
<dd> Turn on and off Renaldo Recuerdo&#8217;s <i>hop.</i></p>
<dt><code>-/+jong</code></p>
<dd> Turn on and off Jong&#8217;s <i>hop.</i></p>
<dt><code>-/+sine</code></p>
<dd> Turn on and off Barry Martin&#8217;s sine <i>hop.</i></p>
<dt><code>-pattern</code><i>&nbsp;<wbr>&lt;pattern&gt;</i></p>
<dd> Allows one to set the pattern for <i>juggle.</i></p>
<dt><code>-tail</code><i>&nbsp;<wbr>num</i></p>
<dd> Minimum Trail Length for <i>juggle.</i></p>
<dt><code>-/+real</code></p>
<dd> Turn on/off real-time juggling for <i>juggle.</i> <code>Deprecated.</code> There should be no need to turn off real-time juggling, even on slow systems. Adjust speed using <code>-count</code>.</p>
<dt><code>-/+describe</code></p>
<dd> Turn on/off pattern descriptions in <i>juggle.</i></p>
<dt><code>-/+balls</code></p>
<dd> Turn on/off Balls in <i>juggle.</i></p>
<dt><code>-/+clubs</code></p>
<dd> Turn on/off Clubs in <i>juggle.</i></p>
<dt><code>-/+torches</code></p>
<dd> Turn on/off Flaming Torches in <i>juggle.</i></p>
<dt><code>-/+knives</code></p>
<dd> Turn on/off Knives in <i>juggle.</i></p>
<dt><code>-/+rings</code></p>
<dd> Turn on/off Rings in <i>juggle.</i></p>
<dt><code>-/+bballs</code></p>
<dd> Turn on/off Bowling Balls in <i>juggle.</i></p>
<dt><code>-/+planetary</code></p>
<dd> Turn on and off planetary gears in <i>gears.</i></p>
<dt><code>-planetsize</code><i>&nbsp;<wbr>num</i></p>
<dd> Sets the size of the screen for planetary option in <i>gears.</i> This is for machines with slower CPU. (Set to 0 for full screen).</p>
<dt><code>-/+disconnected</code></p>
<dd> Turn on and off disconnected pen movement in <i>kaleid.</i></p>
<dt><code>-/+alternate</code></p>
<dd> Turn on and off alternate rotated display mode <i>kaleid.</i></p>
<dt><code>-/+quad</code></p>
<dd> Turn on and off quad mirrored/rotated mode similar to size 4 in <i>kaleid.</i></p>
<dt><code>-/+oct</code></p>
<dd> Turn on and off oct mirrored/rotated mode similar to size 8 in <i>kaleid.</i></p>
<dt><code>-/+linear</code></p>
<dd> Turn on and off Cartesian/Polar coordinate mode in <i>kaleid.</i></p>
<dt><code>-/+conway</code></p>
<dd> Turn on and off John Conway&#8217;s original Life rule S23/B3 <i>life.</i></p>
<dt><code>-/+highlife</code></p>
<dd> Turn on and off David Bell&#8217;s HighLife rule S23/B36 <i>life.</i></p>
<dt><code>-/+daynight</code></p>
<dd> Turn on and off Nathan Thompson&#8217;s Day and Night rule S34678/B3678 <i>life.</i></p>
<dt><code>-/+callahan</code></p>
<dd> Turn on and off Paul Callahan&#8217;s S2b34/B2a hexagonal <i>life.</i></p>
<dt><code>-/+andreen</code></p>
<dd> Turn on and off Bob Andreen&#8217;s S2a2b4a/B2a3a4b hexagonal <i>life.</i></p>
<dt><code>-/+trilife</code></p>
<dd> Turn on and off Carter Bays&#8217; S34/B45 triangular <i>life.</i></p>
<dt><code>-/+trilife1</code></p>
<dd> Turn on and off Carter Bays&#8217; S45/B456 triangular <i>life.</i></p>
<dt><code>-/+trilife2</code></p>
<dd> Turn on and off Carter Bays&#8217; S23/B45 triangular <i>life.</i></p>
<dt><code>-/+totalistic</code></p>
<dd> Turn on and off totalistic rules for <i>life1d.</i> If this is off then it follows rules of the LCAU collection. These rules may not be symmetric and are more general.</p>
<dt><code>-/+additive</code></p>
<dd> Turn on and off additive functions mode in <i>lisa.</i></p>
<dt><code>-/+dissolve</code></p>
<dd> Turn on and off disolving state in <i>loop.</i></p>
<dt><code>-/+evolve</code></p>
<dd> Turn on and off Evolving Loops in <i>loop.</i></p>
<dt><code>-/+langton</code></p>
<dd> Turn on and off Langton Loops for <i>loop.</i></p>
<dt><code>-/+sheath</code></p>
<dd> Turn on and off sheath extension for <i>loop.</i></p>
<dt><code>-/+wrap</code></p>
<dd> Turn on and off wrapping of borders for <i>loop.</i></p>
<dt><code>-increment</code><i>&nbsp;<wbr>num</i></p>
<dd> Sets the option for increasing orders in <i>mandelbrot.</i></p>
<dt><code>-/+alpha</code></p>
<dd> Turn on and off interior displaying level of closest return in <i>mandelbrot.</i></p>
<dt><code>-/+binary</code></p>
<dd> Turn on and off binary decomposition color modulation in <i>mandelbrot.</i></p>
<dt><code>-/+dem</code></p>
<dd> Turn on and off Distance Estimator Method (instead of escape time) in <i>mandelbrot.</i></p>
<dt><code>-/+index</code></p>
<dd> Turn on and off interior displaying iteration of closest return in <i>mandelbrot.</i></p>
<dt><code>-/+lyap</code></p>
<dd> Turn on and off interior displaying according to an estimate of the Lyapunov exponent in <i>mandelbrot.</i></p>
<dt><code>-/+pow</code></p>
<dd> Turn on and off adding z^z in <i>mandelbrot.</i></p>
<dt><code>-/+sin</code></p>
<dd> Turn on and off adding sin(z) in <i>mandelbrot.</i></p>
<dt><code>-/+noants</code></p>
<dd> Turn off and on ants in <i>moebius.</i></p>
<dt><code>-/+solidmoebius</code></p>
<dd> Turn on and off solid Mobius strip in <i>moebius.</i></p>
<dt><code>-/+atoms</code></p>
<dd> Turn on and off the drawing of spheres for the atoms in <i>molecule.</i></p>
<dt><code>-/+bbox</code></p>
<dd> Turn on and off showing the molecules in a blue box in <i>molecule.</i></p>
<dt><code>-/+bonds</code></p>
<dd> Turn on and off the drawing of the atomic bonds in <i>molecule.</i></p>
<dt><code>-molecule</code><i>&nbsp;<wbr>filename</i></p>
<dd> Read a molecule structure from a pdb file in <i>molecule.</i></p>
<dt><code>-/+labels</code></p>
<dd> Turn on and off the labeling of the atoms in <i>molecule.</i></p>
<dt><code>-spin</code><i>{x|y|z}</i></p>
<dd> Set the axis for molecule rotation in <i>molecule.</i> The default is &quot;XYZ&quot;.</p>
<dt><code>+spin</code></p>
<dd> Turn off the molecule rotation in <i>molecule.</i></p>
<dt><code>-/+titles</code></p>
<dd> Turn on and off the molecule description in <i>molecule.</i></p>
<dt><code>-/+wander</code></p>
<dd> Turn on and off the moving of the molecule on a sinoid curve in <i>molecule.</i> Turn on and off movements in <i>fire.</i></p>
<dt><code>-/+ammann</code></p>
<dd> Turn on and off lines for <i>penrose.</i></p>
<dt><code>-increment</code><i>&nbsp;<wbr>value</i></p>
<dd> Allows fine adjustments to order in <i>mandelbrot.</i></p>
<dt><code>-/+erase</code></p>
<dd> Turn on and off erasing for <i>spline.</i> If this option is on, <i>cycles</i> is divided by 64 to compute the number of lines, so as to be compatible when using -fullrandom.</p>
<dt><code>-factory</code><i>&nbsp;<wbr>num</i></p>
<dd> Number of extra factory parts in <i>pipes.</i></p>
<dt><code>-/+fisheye</code></p>
<dd> Turn on if you want a zoomed-in view of <i>pipes.</i></p>
<dt><code>-/+tightturns</code></p>
<dd> Turn on if you want the <i>pipes</i> to bend more often.</p>
<dt><code>-/+rotatepipes</code></p>
<dd> Turn on if you want the pipe system rotated in <i>pipes.</i></p>
<dt><code>-/+complete</code></p>
<dd> Turn on or off complete graph morphing in <i>qix.</i></p>
<dt><code>-msg</code><i>&nbsp;<wbr>textstring</i></p>
<dd> Allows one to pass different explosion elements to <i>pyro2.</i> The explosion types is one of &amp;0, &amp;1, &#8230; &amp;9, &amp;a, &#8230; &amp;f each of which presents a different type of explosion. Normal text can be sent, the string may contain blanks if quoted. An operation system logo will be shown, if the # sign is sent.</p>
<dt><code>-fnt</code><i>&nbsp;<wbr>font</i></p>
<dd> Allows one to pass different elements to <i>pyro2.</i></p>
<dt><code>-size[xyz]</code><i>&nbsp;<wbr>num</i></p>
<dd> Number represents the number of cubies on the x, y, or z axis. Negative numbers offer randomness from 2 to the absolute value of the number. <i>star.</i></p>
<dt><code>-/+hideshuffling</code></p>
<dd> Turn on or off hidden shuffle phase for <i>rubik</i> and <i>skewb.</i></p>
<dt><code>-/+border</code></p>
<dd> Turn on or off borders in <i>shape.</i></p>
<dt><code>-/+shadowing</code></p>
<dd> Turn on or off shadowing in <i>shape.</i></p>
<dt><code>-/+stippling</code></p>
<dd> Turn on or off stippling in <i>shape.</i></p>
<dt><code>-intensity</code><i>&nbsp;<wbr>value</i></p>
<dd> Set the brightness (default 2185) of the sierpinski structure for <i>sierpinski3d.</i></p>
<dt><code>-maxdepth</code><i>&nbsp;<wbr>value</i></p>
<dd> Set the maximum depth (up to 10) of the sierpinski structure for <i>sierpinski3d.</i></p>
<dt><code>-speed</code><i>&nbsp;<wbr>value</i></p>
<dd> Determines after how much steps the depth changes for <i>sierpinski3d.</i></p>
<dt><code>-trek</code><i>&nbsp;<wbr>num</i></p>
<dd> If its a high number you will see the space ship all the time in <i>star.</i></p>
<dt><code>-/+rock</code></p>
<dd> Turn on and off rocks for <i>star.</i> If this is off, stars will be seen instead.</p>
<dt><code>-/+straight</code></p>
<dd> Turn on if <i>star</i> gets you motion sick.</p>
<dt><code>-cyclepeed</code><i>&nbsp;<wbr>num</i></p>
<dd> Set speed of cycling in <i>starfish.</i></p>
<dt><code>-rotation</code><i>&nbsp;<wbr>num</i></p>
<dd> Set rotation velocity in <i>starfish.</i></p>
<dt><code>-thickness</code><i>&nbsp;<wbr>num</i></p>
<dd> Set thickness in <i>starfish.</i></p>
<dt><code>-/+rock</code></p>
<dd> Turn on and off blob for <i>starfish.</i></p>
<dt><code>-spinspeed</code><i>&nbsp;<wbr>num</i></p>
<dd> Set speed of rotation, in degrees per frame for <i>superquadrics.</i></p>
<dt><code>-/+bonus</code></p>
<dd> Turn on in <i>tetris</i> to see 5 square bonus pieces.</p>
<dt><code>-/+well</code></p>
<dd> Turn on in <i>tetris</i> to see welltris.</p>
<dt><code>-ttfont</code><i>&nbsp;<wbr>filename</i></p>
<dd> Sets the True Type font file (or font directory) used for <i>text3d</i></p>
<dt><code>-extrusion</code><i>&nbsp;<wbr>num</i></p>
<dd> Sets length of the text extrusion for <i>text3d</i></p>
<dt><code>-rot_amplitude</code><i>&nbsp;<wbr>float</i></p>
<dd> Sets rotation amplitude value of each letter for <i>text3d</i></p>
<dt><code>-rot_frequency</code><i>&nbsp;<wbr>float</i></p>
<dd> Sets rotation frequency for <i>text3d</i></p>
<dt><code>-/+no_split</code></p>
<dd> Turn on and off word splitting for <i>text3d</i></p>
<dt><code>-ttanimate</code><i>&nbsp;<wbr>function_name</i></p>
<dd> Sets the animation function used for <i>text3d.</i> Currently one of : Random &nbsp;<wbr>FullRandom &nbsp;<wbr>Default &nbsp;<wbr>Default2 &nbsp;<wbr>None &nbsp;<wbr>Crazy &nbsp;<wbr>UpDown &nbsp;<wbr>Extrude &nbsp;<wbr>RotateXY &nbsp;<wbr>RotateYZ &nbsp;<wbr>Frequency &nbsp;<wbr>Amplitude</p>
<dt><code>-speed </code><i>km/h</i></p>
<dd> The speed for all planes in km/h for <i>xcl.</i></p>
<dt><code>-frametime </code><i>microseconds</i></p>
<dd> The time for one frame on the screen. This time is used to calculate the delay time and depends on the speed of the X server for <i>xcl.</i></p>
<dt><code>-line_length </code><i>mm</i></p>
<dd> The distance between the pilot and the plane for <i>xcl.</i></p>
<dt><code>-spectator </code><i>mm</i></p>
<dd> The distance between spectator and pilot. It should be grater than the line_length and the half wing width of the plane to be not dangerous for the spectator for <i>xcl.</i></p>
<dt><code>-viewmodel</code></p>
<dd> Shows an animated view of one model for <i>xcl.</i></p>
<dt><code>-/+oldcolor</code></p>
<dd> Sets the colors for the first two planes fixed to red and yellow in <i>xcl.</i></p>
<dt><code>-xcldebug</code></p>
<dd> Shows some additional timing information to make sure that the calibrate procedure goes right in <i>xcl.</i></p>
<dt><code>-automatic</code></p>
<dd> The auto scale for automatic fit into the window is <i>De</i>activated with this option for <i>xcl.</i></p>
<dt><code>-randomstart</code></p>
<dd> Use a random start point for models at startup for <i>xcl.</i></p>
<dt><code>-duration</code><i>&nbsp;<wbr>seconds</i></p>
<dd> Allows one to set a duration for a mode in <i>random.</i> Duration of 0 is defined as infinite.</p>
<dt><code>-/+fullrandom</code></p>
<dd> Turn on/off randomness options within modes in <i>random.</i> Not implemented for all mode options.</p>
<dt><code>-modelist</code><i>&nbsp;<wbr>textstring</i></p>
<dd> Allows one to pass a list of files to randomly display to <i>random.</i> &quot;all&quot; will get all files but blank (and bomb if compiled in). &quot;all,blank&quot; will get all modes. &quot;all,-image bounce,+blank&quot; will get all modes excluding image and bounce modes. &quot;bug wator&quot; will get only bug and wator. &quot;allgl&quot; will get only the GL modes if compiled in, all-allgl will get all excluding the GL modes, &quot;allnice&quot; will weed out high cpu usage modes (as well as hackers and gl modes). &quot;allxpm&quot; will get all modes that use xpm. &quot;allwrite&quot; will get all modes that take advantage of writable colormaps (not including xpm). &quot;all3d&quot; will get all the modes that support this option. &quot;allmouse&quot; will get all the modes that support mouse interaction. Similarly, &quot;allautomata&quot; for automata modes, &quot;allfractal&quot; for fractal modes, &quot;allgeometry&quot; for geometry modes, &quot;allspace&quot; for space modes. The random mode itself can not be referenced.</p>
<dt><code>-/+sequential</code></p>
<dd> Turn on non-random <i>random</i> option. </p>
</dl>
<h2>**WARNING**</h2>
<p> <code>xlock</code> can appear to hang if it is competing with a high-priority process for the CPU. For example, if <code>xlock</code> is started after a process with &#8216;nice -20&#8217; (high priority), <code>xlock</code> will take considerable amount of time to respond. </p>
<h2>SHADOW PASSWORDS</h2>
<p> If the machine is using a shadow password system, then <code>xlock</code> may not be set up to get the real password and so must be given one of its own. This can be either on the command line, via the <code>-cpasswd</code> option, or in the file <code>$HOME/.xlockrc</code>, with the first taking precedence. In both cases an encrypted password is expected (see <a href="/docs/linux/man/8-makekey/">makekey</a>(8)). If neither is given, then <code>xlock</code> will prompt for a password and will use that, also storing an encrypted version of it in <code>$HOME/.xlockrc</code> for future use. </p>
<h2>XLOCK AND SSH-AGENT</h2>
<p> If you use <a href="/docs/linux/man/1-ssh-agent/">ssh-agent</a>(1) to avoid entering a passphrase every time you use one of your <a href="/docs/linux/man/1-ssh/">ssh</a>(1) private keys, it&#8217;s good security practice to have ssh-agent forget the keys before you leave your terminal unattended. That way, an attacker who takes over your terminal won&#8217;t be able to use your private ssh keys to log in to other systems. Once you return to your terminal, you can enter the passphrase and re-add the keys to ssh-agent. There are a couple of ways in which <code>xlock</code> can help to automate this process. Firstly, the <i>startCmd</i> option allows <code>xlock</code> to be configured to run &#8216;ssh-add -D&#8217; every time you lock the screen, so that your keys are automatically deleted from ssh-agent. If the passphrase on your ssh keys is the same as your password, then <code>xlock</code> can also be made to re-add the keys to ssh-agent when you unlock the screen, via the <i>pipepassCmd</i> option. This requires a bit of scripting, as the command must read your password from standard input and then automate the interaction with ssh-add to re-add the keys. There is an example of such a script in the <code>xlock</code> distribution &#8211; see <i>etc/xlockssh*</i> </p>
<h2>BUGS</h2>
<p> &quot;kill -KILL <code>xlock</code> &quot; causes the server that was locked to be unusable, since all hosts (including localhost) were removed from the access control list to lock out new X clients, and since <code>xlock</code> could not catch SIGKILL, it terminated before restoring the access control list. This will leave the X server in a state where <i>&quot;you can no longer connect to that server, and this operation cannot be reversed unless you reset the server.&quot;</i> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-From the X11R4 Xlib Documentation, Chapter 7.</p>
<p> NCD terminals do not allow xlock to remove all the hosts from the access control list. Therefore you will need to use the &quot;-remote&quot; and &quot;-allowaccess&quot; switches. If you happen to run without &quot;-allowaccess&quot; on an NCD terminal, <code>xlock</code> will not work and you will need to reboot the terminal, or simply go into the SETUP menus, under &#8216;Network Parameters&#8217;, and turn off TCP/IP access control. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-x/">X</a>(1), Xlib Documentation. </p>
<h2>AUTHOR</h2>
<p> Maintained by:</p>
<dl>
<dt>
<dd> David A. Bagley, &lt;<i>bagleyd AT verizon.net</i>&gt;</dl>
<p> The latest version is currently at:</p>
<dl>
<dt>
<dd> <i><a rel="nofollow" href="http://www.sillycycle.com/xlock">http://www.sillycycle.com/xlock</a></i><br />
 <i><a href="ftp://ibiblio.org/pub/Linux/X11/screensavers">ftp://ibiblio.org/pub/Linux/X11/screensavers</a></i></dl>
<p> Original Author:</p>
<dl>
<dt>
<dd> Patrick J. Naughton, &lt;<i>naughton AT eng.sun.com</i>&gt;<br />
 Mailstop 21-14<br />
 Sun Microsystems Laboratories, Inc.<br />
 Mountain View, CA 94043<br />
 415/336-1080</dl>
<p> with many additional contributors. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1988-1991 by Patrick J. Naughton<br />
 Copyright (c) 1993-2016 by David A. Bagley </p>
<p> Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. </p>
<p> This file is provided AS IS with no warranties of any kind. The author shall have no liability with respect to the infringement of copyrights, trade secrets or any patents by this file or any part thereof. In no event will the author be liable for any lost revenue or profits or<br />
&nbsp;<wbr>other special, indirect and consequential damages.<br />
 The original BSD daemon is Copyright (c) 1988 Marshall Kirk McKusick. All Rights Reserved.<br />
 DEC, HP, IBM, Linux, SCO, SGI, and Sun icons have their respective copyrights. </p>
<h2>Index</h2>
