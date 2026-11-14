---
title: "bzw(5)"
name: "bzw"
section: "5"
letter: "b"
url: "/docs/linux/man/5-bzw/"
description: "bzw – BZFlag world file format"
---

<p>bzw &#8211; BZFlag world file format</p>
<h2>Description</h2>
<p>The BZFlag world file format describes a world environment that is used by the BZFlag game server, bzfs. <i>X BZW file format</i> The BZFlag world file format describes and environment that includes the game map, physical world attributes, and automatic world weapons. The map may contain a variety of &quot;obstacles&quot; like buildings, pyramids, and meshes. These obstacles make up the world that the BZFlag tanks will drive around in. Map attributes may be set to create worlds of various sizes, the default size is 800&#215;800.</p>
<dl>
<dt>Here is small example world:</p>
<dd></dl>
<p> # simple world containing a box, pyramid, and mesh<br />
 <code>world</code><br />
 <code> name</code> Simple World<br />
 <code> size</code> 100.0<br />
 <code>end</code><br />
 <code>box</code><br />
 <code> position</code> -20 -20 0<br />
 <code> size</code> 10 20 10<br />
 <code>end</code><br />
 <code>pyramid</code><br />
 <code> position</code> 20 20 0<br />
 <code> size</code> 10 10 20<br />
 <code>end</code><br />
 <code>mesh</code><br />
 <code> vertex</code> -10 0 0<br />
 <code> vertex</code> 10 0 0<br />
 <code> vertex</code> 0 10 0<br />
 <code> face</code><br />
 <code> vertices</code> 0 1 2<br />
 <code> endface</code><br />
 <code>end</code><br />
 The .bzw file is a plain text file with a relatively simple file format. The format of this text file consists of any number of objects listed in any order (except that physics, textureMatrix, dynamicColor, and material must come before they are referenced) separated by newlines and grouped into blocks of types. The list of world types consists of:<br />
 <code>world</code><br />
 <code>options</code><br />
 <code>waterLevel</code><br />
 <code>dynamicColor</code><br />
 <code>textureMatrix</code><br />
 <code>transform</code><br />
 <code>material</code><br />
 <code>physics</code><br />
 <code>define</code><br />
 <code>group</code><br />
 <code>mesh</code><br />
 <code>meshbox</code><br />
 <code>meshpyr</code><br />
 <code>arc</code><br />
 <code>cone</code><br />
 <code>sphere</code><br />
 <code>tetra</code><br />
 <code>box</code><br />
 <code>pyramid</code><br />
 <code>link</code><br />
 <code>teleporter</code><br />
 <code>base</code><br />
 <code>weapon</code><br />
 <code>zone</code><br />
 Each object is described by placing the type on one line, the word <i>end</i> on a following line, and a list of attributes for that object, one per line, in between. The exceptions to the rule are <i>define</i> and <i>face</i>, which are concluded with <i>enddef</i> and <i>endface</i>. Attributes may be listed in any order. Attributes have default values, and if that is good enough, the attribute need not be listed. Words are always specified in lowercase. Line comments can be specified by placing a # sign at the start of the line. For documentation purposes, you can tag each object by adding a name attribute. There is no set limit to the number of times you may use any of the objects except for the world, options, and waterLevel objects, they can only be specified once. The options object contains command line arguments that are used to configure the server&#8217;s game mode, but can not contain server specific options such as -p, -passwd, and -conf.<br />
 In the following examples, the values are the defaults. <code>The World object</code><br />
 Header for the world. <code>world</code><br />
 <code> name</code> example_world<br />
 <code> size</code> 400.0<br />
 <code> flagHeight</code> 10.0<br />
 <code>end</code><br />
 <code>The Options object</code><br />
 A world file interface for setting command line options for BZFS. <code>options</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-set&nbsp;<wbr>_tankSpeed 36 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-j&nbsp;<wbr>+r -ms 3 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>+f GM{5}&nbsp;<wbr>+f SW{5}<br />
 <code>end</code><br />
 <code>The Water Level object</code><br />
 Sets how high the water is, in a matter of units. <code>waterLevel</code><br />
 <code> name</code> example_waterlevel<br />
 <code> height</code> -1.0 # anything below 0 turns it off<br />
 <code>end</code><br />
 <code>The Group Definition object</code><br />
 Defines a group, which may include other group instances<br />
 This does not place any objects into the world, a group instance must be used to generate world objects from a group definition. <code>define</code> &lt;example_groupdef&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>You can add any object to a group definition, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>except for the following types: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>textureMatrix </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>dynamicColor </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>material </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>physics </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>links </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>weapon </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>zone<br />
 <code>enddef</code><br />
 <code>The Group Instantiation object</code><br />
 Instantiates a group, and possibly modifies subobjects <code>group</code> &lt;example_groupdef&gt; # a valid group definition reference<br />
 <code> shift</code> 0 0 0 # (<code>repeatable</code>)<br />
 <code> scale</code> 1 1 1 # (<code>repeatable</code>)<br />
 <code> shear</code> 0 0 0 # (<code>repeatable</code>)<br />
 <code> spin</code> angle nx ny nz # (<code>repeatable</code>) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>angle degrees about vector n<br />
 <code> team</code> 0 # change all base colors within group<br />
 <code> tint</code> 1 1 1 1 # hierarchically tints objects within this group<br />
 <code> drivethrough</code> # make all subobjects drivethrough<br />
 <code> shootthrough</code> # make all subobjects shootthrough<br />
 <code> phydrv</code> example_phydrv # reassign any valid physics drivers<br />
 <code> matref</code> example_material # set material properties </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>(except for the color)<br />
 <code>end</code><br />
 <code>The Dynamic Color object</code> <code>dynamicColor</code><br />
 <code> name</code> example_dyncol </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>there are 4 channels that can be modified: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>red</code>,&nbsp;<wbr><code>green</code>,&nbsp;<wbr><code>blue</code>,&nbsp;<wbr><code>alpha</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>there are 5 types of commands per channel: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>limits</code>,&nbsp;<wbr><code>sinusoid</code>,&nbsp;<wbr><code>clampUp</code>,&nbsp;<wbr><code>clampDown</code>,&nbsp;<wbr><code>sequence</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>except for&nbsp;<wbr>&quot;limits&quot;&nbsp;<wbr>and&nbsp;<wbr>&quot;sequence&quot;, the commands are&nbsp;<wbr><code>repeatable</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>if a sequence is used, then clampUps and clampDowns have no effect </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>sequences can use three states&nbsp;<wbr>(0, 1, 2). </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0 &#8211; equivalent to an active clampDown </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1 &#8211; equivalent to no clamps </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2 &#8211; equivalent to an active clampUp </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>if both clampUp and clampDown are active, the value is&nbsp;<wbr>(min+max)/2 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>the sinusoid function starts at the max value </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>the sum of a channel&#8217;s sinusoids is clamped between 0 and 1<br />
 <code> red limits</code> 0 1 # min/max limits<br />
 <code> green sinusoid</code> 0.1 0 0.25 # period, offset, weight<br />
 <code> blue clampUp</code> 0.1 0 0.75 # period, offset, width<br />
 <code> alpha clampDown</code> 0.2 0.5 0.5 # period, offset, width<br />
 <code> red sequence</code> 0.0 0.0 2 0 1 1 2 0 &#8230; # period, offset, list of states<br />
 <code>end</code><br />
 <code>The Texture Matrix object</code> <code>textureMatrix</code><br />
 <code> name</code> example_texmat<br />
 <code> scale</code> 0.0 0.0 1.0 1.0 # u/v freqs, u/v scales<br />
 <code> spin</code> 0.0 # rotation freq<br />
 <code> shift</code> 0.0 0.0 # u/v freqs<br />
 <code> center</code> 0.5 0.5 # dynamic u/v center (for spin and scale)<br />
 <code> fixedscale</code> 0.0 0.0 # time invariant u/v scale<br />
 <code> fixedspin</code> 0.0 # time invariant rotation<br />
 <code> fixedshift</code> 0.0 0.0 # time invariant u/v shift<br />
 <code>end</code><br />
 <code>Material Properties</code> Material properties may be set on several types of objects, including meshes, mesh faces, arcs, cones, spheres, and tetras. Here are the properties:<br />
 <code>material</code><br />
 <code> name</code> example_material<br />
 <code> resetmat</code> # restore default values<br />
 <code> matref</code> material_name # copy another material&#8217;s properties<br />
 <code> ambient</code> 0.2 0.2 0.2 1.0 # ambient color<br />
 <code> diffuse</code> 1.0 1.0 1.0 1.0 # diffuse color (<code>main color</code>)<br />
 <code> color</code> 1.0 1.0 1.0 1.0 # synonym for &#8216;diffuse&#8217;<br />
 <code> specular</code> 0.0 0.0 0.0 1.0 # specular color<br />
 <code> emission</code> 0.0 0.0 0.0 1.0 # emission color<br />
 <code> shininess</code> 0.0 # shininess (0.0 &#8211; 128.0)<br />
 <code> texture</code> filename # set working texture </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&#8211; non-interlaced PNG </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&#8211; http://&nbsp;<wbr>or ftp://&nbsp;<wbr>hyperlinks can be used&nbsp;<wbr>&nbsp;<wbr>(no spaces) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&#8211; BZFlag default texture names can be used&nbsp;<wbr>&nbsp;<wbr>(.png not required)<br />
 <code> addtexture</code> filename # add texture<br />
 <code> notextures</code> # specify that no textures are to be used<br />
 <code> notexalpha</code> # don&#8217;t use the texture&#8217;s alpha channel<br />
 <code> notexcolor</code> # the color is not applied to the texture </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>if a texture is specified, but not found, the default texture </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>will be used. if the default texture is also not available, then </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>the color will be used&nbsp;<wbr>(untextured)<br />
 <code> spheremap</code> # use spherical texture coordinate mapping<br />
 <code> texmat</code> -1 # texture matrix (-1 for none)<br />
 <code> dyncol</code> -1 # dynamic color (-1 for none)<br />
 <code> noradar</code> # do not display on radar (except normal mode)<br />
 <code> noshadow</code> # do not render shadows<br />
 <code> noculling</code> # do not cull by face winding (double-sided)<br />
 <code> nosorting</code> # do not do front-to-back alpha sorting<br />
 <code> nolighting</code> # disable lighting<br />
 <code> alphathresh 0.0</code> # alpha thresholding value<br />
 <code> groupalpha</code> # sort translucent faces as a group<br />
 <code> occluder</code> # faces with this material will occlude<br />
 <code>end</code><br />
 <code>The Physics Driver object</code> <code>physics</code><br />
 <code> name</code> example_phydrv<br />
 <code> linear</code> 0.0 0.0 0.0 # x/y/z linear velocities<br />
 <code> angular</code> 0.0 0.0 0.0 # rotation freq, x/y coordinates<br />
 <code> slide</code> 0.0 # time until max velocity (&gt; 0.0 enables)<br />
 <code> death</code> Message goes here. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>the&nbsp;<wbr>&#8216;death&#8217;&nbsp;<wbr>property requires a non-blank message<br />
 <code>end</code><br />
 <code>The Mesh object</code> <code>mesh</code><br />
 <code> name</code> example_mesh </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Material properties applied to a mesh apply to all faces </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>that follow the setting. Mesh faces will alter their own </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>properties without affecting the state of the mesh properties. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>The same pattern is used to apply physics drivers.<br />
 <code> vertex</code> 100 200 300 # add a vertex (<code>repeatable</code>)<br />
 <code> normal</code> 1.0 0 0 # add a normal (<code>repeatable</code>)<br />
 <code> texcoord</code> 0.1 0.75 # add a texture coordinate (<code>repeatable</code>)<br />
 <code> inside</code> 5.5 4.5 1.2 # add an inside point (<code>repeatable</code>)<br />
 <code> outside</code> 0 0 1000 # add an outside point (<code>repeatable</code>)<br />
 <code> shift</code> 0 0 0 # (<code>repeatable</code>)<br />
 <code> scale</code> 1 1 1 # (<code>repeatable</code>)<br />
 <code> shear</code> 0 0 0 # (<code>repeatable</code>)<br />
 <code> spin</code> angle nx ny nz # (<code>repeatable</code>)<br />
 <code> phydrv</code> example_phydrv # assign a physics driver<br />
 <code> smoothbounce</code> # ricochets use normals<br />
 <code> noclusters</code> # render each mesh face individually<br />
 <code> face</code> # start a face (<code>repeatable</code>) </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>the front-face winding is counter-clockwise<br />
 <code> vertices</code> 1 4 0 3 5 # list of vertices (requires at least three)<br />
 <code> normals</code> 2 6 0 4 7 # list of normals (optional)<br />
 <code> texcoords</code> 0 3 2 4 9 # list of texture coordinates (optional)<br />
 <code> phydrv</code> example_phydrv # assign a physics driver<br />
 <code> endface</code> # end the face </p>
<p>&nbsp;<wbr>&nbsp;<wbr># </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>This next element can be added to increase the rendering speed </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>of the mesh object. If the client is capable of using this data, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>then it is used to draw the mesh instead of the face information. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#<br />
 <code> drawInfo</code><br />
 <code> dlist</code> # display list for all material sets<br />
 <code> decorative</code> # older clients with not see this mesh<br />
 <code> angvel</code> &lt;degrees/sec&gt; # rotation about initial Z axis<br />
 <code> extents</code> &lt;minX&gt; &lt;minY&gt; &lt;minZ&gt; &lt;maxX&gt; &lt;maxY&gt; &lt;maxZ&gt;<br />
 <code> sphere</code> &lt;x&gt; &lt;y&gt; &lt;z&gt; &lt;radiusSquared&gt;<br />
 <code> corner</code> &lt;v&gt; &lt;n&gt; &lt;t&gt; (<code>repeatable</code>)<br />
 <code> vertex</code> 0.0 0.0 0.0 (<code>repeatable</code>)<br />
 <code> normal</code> 0.0 0.0 0.0 (<code>repeatable</code>)<br />
 <code> texcoord</code> 0.0 0.0 (<code>repeatable</code>)<br />
 <code> lod</code> (<code>repeatable</code>)<br />
 <code> lengthPerPixel</code> &lt;value&gt;<br />
 <code> matref</code> &lt;name&gt; (<code>repeatable</code>)<br />
 <code> dlist</code> # display list for this material set<br />
 <code> sphere</code> &lt;x&gt; &lt;y&gt; &lt;z&gt; &lt;radiusSquared&gt;<br />
 <code> points</code> 0 (<code>repeatable</code>)<br />
 <code> lines</code> 0 1 (<code>repeatable</code>)<br />
 <code> lineloop</code> 0 1 (<code>repeatable</code>)<br />
 <code> linestrip</code> 0 1 (<code>repeatable</code>)<br />
 <code> tris</code> 0 1 2 (<code>repeatable</code>)<br />
 <code> tristrip</code> 0 1 2 (<code>repeatable</code>)<br />
 <code> trifan</code> 0 1 2 (<code>repeatable</code>)<br />
 <code> quads</code> 0 1 2 3 (<code>repeatable</code>)<br />
 <code> quadstrip</code> 0 1 2 3 (<code>repeatable</code>)<br />
 <code> polygon</code> 0 1 2 (<code>repeatable</code>)<br />
 <code> end</code> # matref<br />
 <code> end</code> # lod<br />
 <code> end</code> # drawInfo<br />
 <code>end</code> # mesh<br />
 <code>The Arc object</code> <code>arc</code><br />
 <code> name</code> example_arc<br />
 <code> divisions 16</code> # number of subdivisions<br />
 <code> flatshading</code> # flat shading (smooth is default)<br />
 <code> angle 360</code> # the sweep angle<br />
 <code> ratio 1</code> # (outrad &#8211; inrad) / outrad<br />
 <code> position</code> 0.0 0.0 0.0<br />
 <code> size</code> 10 10 10<br />
 <code> rotation</code> 0.0<br />
 <code> shift</code> 0 0 0 # (<code>repeatable</code>)<br />
 <code> scale</code> 1 1 1 # (<code>repeatable</code>)<br />
 <code> shear</code> 0 0 0 # (<code>repeatable</code>)<br />
 <code> spin</code> angle nx ny nz # (<code>repeatable</code>)<br />
 <code> phydrv</code> example_phydrv # assign a physics driver<br />
 <code> smoothbounce</code> # ricochets use normals<br />
 <code>end</code><br />
 <code>The Cone object</code> <code>cone</code><br />
 <code> name</code> example_cone<br />
 <code> divisions 16</code> # number of subdivisions<br />
 <code> flatshading</code> # flat shading (smooth is default)<br />
 <code> angle 360</code> # the sweep angle<br />
 <code> position</code> 0.0 0.0 0.0<br />
 <code> size</code> 10 10 10<br />
 <code> rotation</code> 0.0<br />
 <code> shift</code> 0 0 0 # (<code>repeatable</code>)<br />
 <code> scale</code> 1 1 1 # (<code>repeatable</code>)<br />
 <code> shear</code> 0 0 0 # (<code>repeatable</code>)<br />
 <code> spin</code> angle nx ny nz # (<code>repeatable</code>)<br />
 <code> phydrv</code> example_phydrv # assign a physics driver<br />
 <code> smoothbounce</code> # ricochets use normals<br />
 <code>end</code><br />
 <code>The Sphere object</code> <code>sphere</code><br />
 <code> name</code> example_sphere<br />
 <code> divisions 4</code> # number of subdivisions<br />
 <code> flatshading</code> # flat shading (smooth is default)<br />
 <code> position</code> 0.0 0.0 10.0<br />
 <code> size</code> 10 10 10<br />
 <code> radius 10</code> # sets all size values to this value<br />
 <code> rotation</code> 0.0<br />
 <code> shift</code> 0 0 0 # (<code>repeatable</code>)<br />
 <code> scale</code> 1 1 1 # (<code>repeatable</code>)<br />
 <code> shear</code> 0 0 0 # (<code>repeatable</code>)<br />
 <code> spin</code> angle nx ny nz # (<code>repeatable</code>)<br />
 <code> phydrv</code> example_phydrv # assign a physics driver<br />
 <code> smoothbounce</code> # ricochets use normals<br />
 <code>end</code><br />
 <code>The Tetrahedron object</code> <code>tetra</code><br />
 <code> name</code> example_tetra<br />
 # there must always be 4 vertices<br />
 <code> vertex</code> -10.0 -5.0 0.0<br />
 <code> vertex</code> +10.0 -5.0 0.0<br />
 <code> vertex</code> 0.0 10.0 0.0<br />
 <code> vertex</code> 0.0 5.0 10.0<br />
 <code> shift</code> 0 0 0 # (<code>repeatable</code>)<br />
 <code> scale</code> 1 1 1 # (<code>repeatable</code>)<br />
 <code> shear</code> 0 0 0 # (<code>repeatable</code>)<br />
 <code> spin</code> angle nx ny nz # (<code>repeatable</code>)<br />
 <code>end</code><br />
 <code>The Box object</code><br />
 Adds a simple block. <code>box</code><br />
 <code> name</code> example_box<br />
 <code> position</code> 0.0 0.0 0.0<br />
 <code> size</code> 30.0 30.0 9.42<br />
 <code> rotation</code> 0.0<br />
 <code>end</code><br />
 <code>The Pyramid object</code><br />
 Adds a triangular shaped object. <code>pyramid</code><br />
 <code> name</code> example_pyramid<br />
 <code> position</code> 0.0 0.0 0.0<br />
 <code> size</code> 8.2 8.2 10.25<br />
 <code> rotation</code> 0.0<br />
 <code>end</code><br />
 <code>The Teleporter object</code><br />
 Adds an object that places a tank at another teleporter in a different area when ran through. <code>teleporter</code> [name]<br />
 # the [name] tag is used for linkage<br />
 <code> name</code> example_teleporter<br />
 <code> position</code> 0.0 0.0 0.0<br />
 <code> size</code> 5.06 4.48 20.16<br />
 <code> rotation</code> 0.0<br />
 <code> border</code> 1.12<br />
 <code>end</code><br />
 <code>The Link object</code><br />
 Adds a route to teleport a tank between two teleporters. # Teleporter names are terminated with either :f (forward)<br />
 # or :b (backwards). The forwards link points to 0 degrees,<br />
 # and the backwards link points to 180. Links are made by<br />
 # pattern matching the teleporter names. The &#8216;*&#8217; and &#8216;?&#8217;<br />
 # globbing characters can be used to make multiple matches.<br />
 # If there are multiple matches for the &quot;to&quot; link, then the<br />
 # destination will be selected randomly between the matches.<br />
 # in-game.<br />
 # NOTE: bzfs -d -d -d -d will print the linkage table. <code>link</code><br />
 <code> name</code> example_link<br />
 # this will link all teleporters randomly to all other teleporters<br />
 <code> from</code> *<br />
 <code> to</code> *<br />
 <code>end</code><br />
 # or, to link between known teleporters examp_tele1(front) and examp_tele2(back) <code>link</code><br />
 <code> name</code> example_realLink<br />
 <code> from</code> examp_tele1:f<br />
 <code> to</code> examp_tele2:b<br />
 <code>end</code><br />
 <code>The Base object</code><br />
 Creates a team base where the corresponding team&#8217;s flag is stored. The oncap option will fire a world weapon of the specified type when the team flag for this base is captured. <code>base</code><br />
 <code> name</code> example_base<br />
 <code> position</code> 0.0 0.0 0.0<br />
 <code> size</code> 60.0 60.0 0.0<br />
 <code> rotation</code> 0.0<br />
 <code> color</code> 0<br />
 <code> oncap</code> V<br />
 <code>end</code><br />
 <code>The Weapon object</code><br />
 Creates a world weapon, or a weapon fired automatically by the world. The weapon can either be timed or be event driven. Timed weapons should use the initdelay and delay fields. Event driven weapons need to use the trigger option to define what the trigger event is. Valid trigger events are; OnCap, for flag capture events. OnSpawn, for player spawn events. OnDie, for player death events. If the weapon is to be triggered only for a specific team then the eventteam option should be used with a team number (1 to 4). A eventteam value of -1 will trigger this weapon for any team. -1 is the default eventteam value. <code>weapon</code><br />
 <code> name</code> example_weapon<br />
 <code> position</code> 0.0 0.0 0.0<br />
 <code> rotation</code> 0.0<br />
 <code> tilt</code> 0.0<br />
 <code> initdelay</code> 10.0<br />
 <code> delay</code> 10.0 3.0 5.0 3.0<br />
 <code> type</code> V<br />
 <code> trigger</code> flagcap<br />
 <code> eventteam</code> V<br />
 <code>end</code><br />
 <code>The Zone object</code><br />
 Specifies a certain range in the world, and what attributes that range has. <code>zone</code><br />
 <code> name</code> example_zone<br />
 <code> position</code> 0.0 0.0 0.0<br />
 <code> size</code> 1.0 1.0 1.0<br />
 <code> rotation</code> 0.0<br />
 # where players may spawn<br />
 <code> team</code> 0 1 2 3 4<br />
 # where flag may spawn<br />
 <code> flag</code> GM SW good bad<br />
 # dropped team flags will fly to the closest safety zone<br />
 <code> safety</code> 1 2 3 4<br />
 # attach a flag to this zone (always spawn in this zone)<br />
 <code> zoneflag</code> GM 3 # type, count (type can be a team flag, ex: R*)<br />
 <code>end</code> </p>
<h2>File Syntax</h2>
<p>The symbol &#8216;?&#8217; means that the item is optional. </p>
<p> The notation {a..b} means that the number of times the item can be present must be between &#8216;a&#8217; and &#8216;b&#8217;, where &#8216;*&#8217; mean infinity. (&#8216;?&#8217; is equivalent to {0..1})</p>
<dl>
<dt>angle := &lt;float&gt;</p>
<dd>
<dt>2dpoint := &lt;float&gt; &lt;float&gt;</p>
<dd>
<dt>3dpoint := &lt;float&gt; &lt;float&gt; &lt;float&gt;</p>
<dd>
<dt>rgbColor := &lt;float&gt; &lt;float&gt; &lt;float&gt;</p>
<dd>
<dt>alpha := &lt;float&gt;</p>
<dd>
<dt>rgbaColor := rgbColor alpha? | &lt;color_name&gt; alpha?</p>
<dd>
<dt>channel := &quot;red&quot; | &quot;green&quot; | &quot;blue&quot; | &quot;alpha&quot;</p>
<dd>
<dt><code>(BZWReader.cxx/parseNormalObject)</code></p>
<dd>
<dt>allObjects :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;box&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;pyramid&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;base&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;link&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;teleporter&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;mesh&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;arc&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;meshbox&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;cone&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;meshpyr&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;sphere&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;tetra&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;weapon&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;zone&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;waterLevel&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;dynamicColor&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;textureMatrix&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;material&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;physics&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;transform&quot;</p>
<dt><code>(BZWReader.cxx/BZWReader::readWorldStream)</code></p>
<dd>Note: Blank lines and lines starting with # are discarded. </p>
<dt>worldStream :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;end&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| allObjects</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;define&quot; &lt;group_name&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;enddef&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;group&quot; &lt;group_name&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;teleporter&quot; &lt;name&gt;?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;options&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;include&quot; &lt;filename&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;world&quot;</p>
<dt><code>(ParseMaterial.cxx/parseMaterials)</code></p>
<dd>
<dt>material :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>object</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;matref&quot; &lt;material_name&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;resetmat&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;dyncol&quot; &lt;dynamic_color_name&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;ambient&quot; rgbaColor</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| (&quot;diffuse&quot; | &quot;color&quot;) rgbaColor</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;specular&quot; rgbaColor</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;emission&quot; rgbaColor</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;shininess&quot; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;texture &lt;texture_name&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;notextures&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;addtexture&quot; &lt;texture_name&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;texmat&quot; &lt;matrix_name&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;notexalpha&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;notexcolor&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;spheremap&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;noradar&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;noshadow&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;noculling&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;nosorting&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;nolighting&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;alphathresh&quot; &lt;value&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;groupalpha&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;occluder&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;shader&quot; &lt;shader_name&gt; # NOT IMPLEMENTED</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;addshader&quot; &lt;shader_name&gt; # NOT IMPLEMENTED</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;noshaders&quot; # NOT IMPLEMENTED</p>
<dt><code>(WorldFileObject:.cxx/WorldFileObject::read)</code></p>
<dd>
<dt>object := &quot;name&quot; &lt;name&gt;</p>
<dd>
<dt><code>(WorldFileLocation.cxx/readWorldFileLocation::read)</code></p>
<dd>
<dt>location :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> (&quot;pos&quot; | &quot;position&quot;) 3dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;size&quot; 3dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| (&quot;rot&quot; | &quot;rotation&quot;) &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;shift&quot; 3dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;scale&quot; 3dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;shear&quot; 3dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;spin&quot; angle 3dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;xform&quot; &lt;transform_name&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| object</p>
<dt><code>(WorldFileObstacle.cxx/WorldFileObstacle::read)</code></p>
<dd>
<dt>obstacle :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;drivethrough&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;shootthrough&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;passable&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| location</p>
<dt><code>(CustomArc.cxx/CustomArc::read)</code></p>
<dd>
<dt>meshbox :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;divisions&quot; &lt;integer&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;angle&quot; angle</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;ratio&quot; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;texsize&quot; &lt;float&gt; &lt;float&gt; &lt;float&gt; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;phydrv&quot; &lt;physics_driver_name&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;smoothbounce&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;flatshading&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| material</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| (&quot;top&quot; | &quot;bottom&quot; | &quot;inside&quot; | &quot;outside&quot; | &quot;startside&quot; | &quot;endside&quot;) material</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| obstacle</p>
<dt>arc :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;divisions&quot; &lt;integer&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;angle&quot; angle</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;ratio&quot; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;texsize&quot; &lt;float&gt; &lt;float&gt; &lt;float&gt; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;phydrv&quot; &lt;physics_driver_name&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;smoothbounce&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;flatshading&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| material</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| (&quot;top&quot; | &quot;bottom&quot; | &quot;inside&quot; | &quot;outside&quot; | &quot;startside&quot; | &quot;endside&quot;) material</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| obstacle</p>
<dt><code>(CustomBase.cxx/CustomBase::read)</code></p>
<dd>
<dt>base :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;color&quot; &lt;integer&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| obstacle</p>
<dt><code>(CustomBox.cxx)</code></p>
<dd>
<dt>box := obstacle</p>
<dd>
<dt><code>(CustomCone.cxx/CustomCone::read)</code></p>
<dd>
<dt>meshpyr :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;divisions&quot; &lt;integer&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;angle&quot; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;texsize&quot; &lt;float&gt; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;phydrv&quot; &lt;physics_driver_name&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;smoothbounce&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;flatshading&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| material</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| (&quot;edge&quot; | &quot;bottom&quot; | &quot;startside&quot; | &quot;endside&quot;) material</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;flipz&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| obstacle</p>
<dt>cone :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;divisions&quot; &lt;integer&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;angle&quot; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;texsize&quot; &lt;float&gt; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;phydrv&quot; &lt;physics_driver_name&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;smoothbounce&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;flatshading&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| material</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| (&quot;edge&quot; | &quot;bottom&quot; | &quot;startside&quot; | &quot;endside&quot;) material</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| obstacle</p>
<dt><code>(CustomDynamicColor.cxx/CustomDynamicColor::read)</code></p>
<dd>
<dt>dynamicColor :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> object</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| channel &quot;limits&quot; &lt;float&gt; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| channel &quot;sinusoid&quot; &lt;float&gt; &lt;float&gt; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| channel &quot;clampup&quot; &lt;float&gt; &lt;float&gt; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| channel &quot;clampdown&quot; &lt;float&gt; &lt;float&gt; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| channel &quot;sequence&quot; &lt;float&gt; &lt;float&gt; (&quot;0&quot; &quot;1&quot; &quot;2&quot;){1..*}</p>
<dt><code>(CustomGate.cxx/CustomGate::read)</code></p>
<dd>
<dt>teleporter :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;border&quot; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;horizontal&quot; # NOT IMPLEMENTED</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| obstacle</p>
<dt><code>(CustomGroup.cxx/CustomGroup::read)</code></p>
<dd>
<dt>group :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;team&quot; &lt;integer&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;tint&quot; rgbaColor</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;phydrv&quot; &lt;physics_driver_name&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;matref&quot; &lt;material_name&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| obstacle</p>
<dt><code>(CustomLink.cxx/CustomLink::read)</code></p>
<dd>
<dt>teleporter_spec :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &lt;integer&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &lt;teleporter_name_with_wilcards&gt; (&quot;:f&quot; | &quot;:b&quot;)?</p>
<dt>link :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;from&quot; &lt;teleporter_spec&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;to&quot; &lt;teleporter_spec&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| object</p>
<dt><code>(MeshDrawInfo.cxx/MeshDrawInfo::parseDrawCmd)</code></p>
<dd>
<dt>drawInfoCmd :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;points&quot; &lt;integer&gt;+</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;lines&quot; &lt;integer&gt; &lt;integer&gt; &lt;integer&gt;{2}*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;lineloop&quot; &lt;integer&gt; &lt;integer&gt;+</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;linestrip&quot; &lt;integer&gt; &lt;integer&gt; &lt;integer{2}*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;tris&quot; &lt;integer&gt; &lt;integer&gt; &lt;integer&gt; &lt;integer&gt;{3}*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;tristrip&quot; &lt;integer&gt; &lt;integer&gt; &lt;integer&gt;+</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;trifan&quot; &lt;integer&gt; &lt;integer&gt; &lt;integer&gt;+</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;quads&quot; &lt;integer&gt; &lt;integer&gt; &lt;integer&gt; &lt;integer&gt; &lt;integer&gt;{4}*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;quadstrip&quot; &lt;integer&gt; &lt;integer&gt; &lt;integer&gt;{2}+</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;polygon&quot; &lt;integer&gt; &lt;integer&gt; &lt;integer&gt; &lt;integer&gt;{3}*</p>
<dt><code>(MeshDrawInfo.cxx/MeshDrawInfo::parseDrawSet)</code></p>
<dd>
<dt>drawInfoSet :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;matref&quot; &lt;material_name&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;dlist&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;sphere&quot; 3dpoint &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| drawInfoCmd</p>
<dt><code>(MeshDrawInfo.cxx/MeshDrawInfo::parseDrawLod)</code></p>
<dd>
<dt>drawInfoLod :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;lod&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;lengthPerPixel&quot; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| drawInfoSet</p>
<dt><code>(MeshDrawInfo.cxx/MeshDrawInfo::parse)</code></p>
<dd>
<dt>drawInfo :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;drawInfo&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;dlist&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;decorative&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;angvel&quot; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;extents&quot; 3dpoint 3dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;sphere&quot; 3dpoint &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;corner&quot; &lt;integer&gt; &lt;integer&gt; &lt;integer&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;vertex&quot; 3dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;normal&quot; 3dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;texcoord&quot; &lt;float&gt; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| drawInfoLod</p>
<dt><code>(CustomMesh.cxx/CustomMesh::read)</code></p>
<dd>
<dt>mesh :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;face&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| face</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;endface&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;inside&quot; 3dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;outside&quot; 3dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;vertex&quot; 3dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;normal&quot; 3dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;texcoord&quot; &lt;float&gt; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;phydrv&quot; &lt;physics_driver_name&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;smoothbounce&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;noclusters&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| drawInfo</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| material</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| obstacle</p>
<dt><code>(CustomMeshFace.cxx/CustomMeshFace::read)</code></p>
<dd>
<dt>face :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;vertices&quot; &lt;integer&gt;{3..*}</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;normals&quot; &lt;integer&gt;{3..*}</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;texcoords&quot; &lt;integer&gt;{3..*}</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;phydrv&quot; &lt;physics_driver_name&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;smoothbounce&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;noclusters&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;drivethrough&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;shootthrough&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;passable&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| material</p>
<dt><code>(CustomMeshTransform.cxx/CustomMeshTransform::read)</code></p>
<dd>
<dt>transform :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;shift&quot; 3dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;scale&quot; 3dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;shear&quot; 3dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;spin&quot; angle 3dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;xform&quot; &lt;transform_name&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| object</p>
<dt><code>(CustomPhysicsDriver.cxx/CustomPhysicsDriver::read)</code></p>
<dd>
<dt>physics :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;linear&quot; 3dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;angular&quot; &lt;float&gt; 2dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;radial&quot; &lt;float&gt; 2dpoint # NOT IMPLEMENTED</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;slide&quot; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;death&quot; &lt;string&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| object</p>
<dt><code>(CustomPyramid.cxx/CustomPyramid::read)</code></p>
<dd>
<dt>pyramid :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;flipz&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| obstacle</p>
<dt><code>(CustomSphere.cxx/CustomSphere::read)</code></p>
<dd>
<dt>sphere :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;divisions&quot; &lt;integer&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;radius&quot; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| (&quot;hemi&quot; | &quot;hemisphere&quot;)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;texsize&quot; &lt;float&gt; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;phydrv&quot; &lt;physics_driver_name&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;smoothbounce&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;flatshading&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| material</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| (&quot;edge&quot; | &quot;bottom&quot;) material</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| obstacle</p>
<dt><code>(CustomTetra.cxx/CustomTetra::read)</code></p>
<dd>Note: At most 4 vertices can be specified.<br />
 Note2: material will apply to all vertices when specified first, otherwise like &quot;normals&quot; and &quot;texcoords&quot; they apply to the previous vertex. </p>
<dt>tetra :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;vertex&quot; 3dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;normals&quot; 3dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;texcoords&quot; 2dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| material</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| obstacle</p>
<dt><code>(CustomTextureMatrix.cxx/CustomTextureMatrix::read)</code></p>
<dd>
<dt>textureMatrix :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;fixedshift&quot; 2dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;fixedscale&quot; 2dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;fixedspin&quot; angle</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;fixedcenter&quot; 2dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;shift&quot; &lt;float&gt; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;spin&quot; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;scale&quot; &lt;float&gt; &lt;float&gt; &lt;float&gt; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;center&quot; 2dpoint</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| object</p>
<dt><code>(CustomWaterLevel.cxx/CustomWaterLevel::read)</code></p>
<dd>
<dt>waterLevel :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;height&quot; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| material</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| object</p>
<dt><code>(CustomWeapon.cxx/CustomWeapon::read)</code></p>
<dd>
<dt>weapon :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;initdelay&quot; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;delay&quot; &lt;float&gt;{1..*}</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;type&quot; &lt;flag_short_name&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| location</p>
<dt><code>(CustomWorld.cxx/CustomWorld::read)</code></p>
<dd>
<dt>world :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;size&quot; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;flagHeight&quot; &lt;float&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| object</p>
<dt><code>(CustomZone.cxx/CustomZone::read)</code></p>
<dd>
<dt>zone :=</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;team&quot; &lt;integer&gt;{1..*}</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;flag&quot; (&quot;good&quot; | &quot;bad&quot; | &lt;flag_short_name&gt;){1..*}</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;safety&quot; &lt;integer&gt;{1..*}</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| &quot;zoneflag&quot; &lt;flag_short_name&gt; &lt;integer&gt;?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| location</p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/6-bzflag/">bzflag</a>(6), <a href="/docs/linux/man/6-bzadmin/">bzadmin</a>(6), <a href="/docs/linux/man/6-bzfs/">bzfs</a>(6) </p>
