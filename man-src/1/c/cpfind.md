---
title: "cpfind(1)"
name: "cpfind"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpfind/"
description: "cpfind – Feature matching for panoramic stitching"
---

<h2 class="name">NAME</h2>
<p> cpfind &#8211; Feature matching for panoramic stitching </p>
<h2>SYNOPSIS</h2>
<p> <code>cpfind</code> [options] -o <i>output_project</i> <i>project.pto</i> </p>
<p> <code>cpfind</code> [options] -k i0 -k i1 [&#8230;] <i>project.pto</i> </p>
<p> <code>cpfind</code> [options] &#8211;kall <i>project.pto</i></p>
<h2>DESCRIPTION</h2>
<p> <code>cpfind</code> cpfind is a control-point detector for Hugin. It expects a project file as input and writes a project file with control-points on success. It depends on reasonable lens information in the input project file. </p>
<p> The first step is the feature description: In this step the images of the project file are loaded and so called keypoints are searched. They describe destinctive features in the image. <code>cpfind</code> uses a gradient based descriptor for the feature description of the keypoints. </p>
<p> In a second step, the feature matching, all keypoints of two images are matched against each other to find features which are on both images. If this matching was successfull two keypoints in the two images become one control point.</p>
<h2>USAGE</h2>
<h3>Rectilinear and fisheye images</h3>
<p> Cpfind can find control points in rectilinear and fisheye images. To achieve good control points images with a high horizontal field of view (e.g. ultra wide rectilinear or fisheye) are therefor remapped into a conformal space (cpfind is using the stereographic projection) and the feature matching occurs in this space. Before writing the control points the coordinates are remapped back to the image space. This happens automatic depending on the information about the lens in the input project file. So check that your input project file contains reasonable information about the used lens.</p>
<h3>Using celeste</h3>
<p> Outdoor panorama often contains clouds. Clouds are bad areas for setting control points because they are moving object. Cpfind can use the same algorithm as celeste_standalone to masked out areas which contains clouds. (This is only done internal for the keypoint finding step and does not change the alpha channel of your image. If you want to generate a mask image use celeste_standalone). To run cpfind with celeste use </p>
<pre>
   cpfind --celeste -o output.pto input.pto
</pre>
<p> Using cpfind with integrated celeste should be superior against using cpfind and celeste_standalone sequential. When running cpfind with celeste areas of clouds, which often contains keypoints with a high quality measure, are disregarded and areas without clouds are used instead. When running cpfind without celeste also keypoints on clouds are found. When afterwards running celeste_standalone these control points are removed. In the worst case all control points of a certain image pair are removed. </p>
<p> So running cpfind with celeste leads to a better &#8220;control point quality&#8221; for outdoor panorama (e.g. panorama with clouds). Running cpfind with celeste takes longer than cpfind alone. So for indoor panorama this option does not need to specified (because of longer computation time). </p>
<p> The celeste step can be fine tuned by the parameters &#8211;celesteRadius and &#8211;celesteThreshold.</p>
<h3>Matching strategy</h3>
<p> <i>All pairs</i> </p>
<p> This is the default matching strategy. Here all image pairs are matched against each other. E.g. if your project contains 5 images then cpfind matches the image pairs: 0-1, 0-2, 0-3, 0-4, 1-2, 1-3, 1-4, 2-3, 2-4 and 3-4 </p>
<p> This strategy works for all shooting strategy (single-row, multi-row, unordered). It finds (nearly) all connected image pairs. But it is computational expensive for projects with many images, because it test many image pairs which are not connected. </p>
<p> <i>Linear match</i> </p>
<p> This matching strategy works best for single row panoramas: </p>
<pre>
   cpfind --linearmatch -o output.pto input.pto
</pre>
<p> This will only detect matches between adjacent images, e.g. for the 5 image example it will matches images pairs 0-1, 1-2, 2-3 and 3-4. The matching distance can be increased with the switch &#8211;linearmatchlen. E.g. with &#8211;linearmatchlen 2 cpfind will match a image with the next image and the image after next, in our example it would be 0-1, 0-2, 1-2, 1-3, 2-3, 2-4 and 3-4. </p>
<p> <i>Multirow matching</i> </p>
<p> This is an optimized matching strategy for single and multi-row panorama: </p>
<pre>
   cpfind --multirow -o output.pto input.pto
</pre>
<p> The algorithm is the same as described in multi-row panorama. By integrating this algorithm into cpfind it is faster by using several cores of modern CPUs and don&#8217;t caching the keypoints to disc (which is time consuming). If you want to use this multi-row matching inside hugin set the control point detector type to All images at once. </p>
<p> <i>Keypoints caching to disc</i> </p>
<p> The calculation of keypoints takes some time. So cpfind offers the possibility to save the keypoints to a file and reuse them later again. With &#8211;kall the keypoints for all images in the project are saved to disc. If you only want the keypoints of particular image use the parameter -k with the image number: </p>
<pre>
   cpfind --kall input.pto
   cpfind -k 0 -k 1 input.pto
</pre>
<p> The keypoint files are saved by default into the same directory as the images with the extension .key. In this case no matching of images occurs and therefore no output project file needs to specified. If cpfind finds keyfiles for an image in the project it will use them automatically and not run the feature descriptor again on this image. If you want to save them to annother directory use the &#8211;keypath switch. </p>
<p> This procedure can also be automate with the switch &#8211;cache: </p>
<pre>
   cpfind --cache -o output.pto input.pto
</pre>
<p> In this case it tries to load existing keypoint files. For images, which don&#8217;t have a keypoint file, the keypoints are detected and save to the file. Then it matches all loaded and newly found keypoints and writes the output project. </p>
<p> If you don&#8217;t need the keyfile longer, the can be deleted automatic by </p>
<pre>
   cpfind --clean input.pto
</pre>
<h2>EXTENDED OPTIONS</h2>
<h3>Feature description</h3>
<p> For speed reasons cpfind is using images, which are scaled to their half width and height, to find keypoints. With the switch &#8211;fullscale cpfind is working on the full scale images. This takes longer but can provide &#8220;better&#8221; and/or more control points. </p>
<p> The feature description step can be fine-tuned by the parameters:</p>
<dl>
<dt><code>&#8211;sieve1width</code> &lt;int&gt;</p>
<dd> Sieve 1: Number of buckets on width (default: 10)</p>
<dt><code>&#8211;sieve1height</code> &lt;int&gt;</p>
<dd> Sieve 1: Number of buckets on height (default: 10)</p>
<dt><code>&#8211;sieve1size</code> &lt;int&gt;</p>
<dd> Sieve 1: Max points per bucket (default: 100)</p>
<dt><code>&#8211;kdtreesteps</code> &lt;int&gt;</p>
<dd> KDTree: search steps (default: 200)</p>
<dt><code>&#8211;kdtreeseconddist</code> &lt;double&gt;</p>
<dd></dl>
<p> KDTree: distance of 2nd match (default: 0.25) </p>
<p> Cpfind stores maximal sieve1width * sieve1height * sieve1size keypoints per image. If you have only a small overlap, e.g. for 360 degree panorama shoot with fisheye images, you can get better results if you increase sieve1size. You can also try to increase sieve1width and/or sieve1height.</p>
<h3>Feature matching</h3>
<p> Fine-tuning of the matching step by the following parameters:</p>
<dl>
<dt><code>&#8211;ransaciter</code> &lt;int&gt;</p>
<dd> Ransac: iterations (default: 1000)</p>
<dt><code>&#8211;ransacdist</code> &lt;int&gt;</p>
<dd> Ransac: homography estimation distance threshold (pixels) (default: 25)</p>
<dt><code>&#8211;ransacmode</code> (auto, hom, rpy, rpyv, rpyb)</p>
<dd> Select the model used in the ransac step. </p>
<p> hom: Assume a homography. Only applicable for non-wide angle<br />
&nbsp;<wbr>&nbsp;<wbr>views. Uses the original panomatic code. It is also more flexible<br />
&nbsp;<wbr>&nbsp;<wbr>than required and can generate false matches, particularly if most<br />
&nbsp;<wbr>&nbsp;<wbr>of the matches are located on a single line. </p>
<p> rpy: Align images using roll, pitch and yaw. This requires a good<br />
&nbsp;<wbr>&nbsp;<wbr>estimate for the horizontal field of view&nbsp;<wbr>(and distortion, for<br />
&nbsp;<wbr>&nbsp;<wbr>heavily distorted images). It is the preferred mode if a<br />
&nbsp;<wbr>&nbsp;<wbr>calibrated lens is used, or the&nbsp;<wbr><font SIZE="-1">HFOV</font>&nbsp;<wbr>could be read successfully<br />
&nbsp;<wbr>&nbsp;<wbr>from the&nbsp;<wbr><font SIZE="-1">EXIF</font>&nbsp;<wbr>data. </p>
<p> rpyv: Align pair by optimizing roll, pitch, yaw and field of<br />
view. Should work without prior knowledge of the field of view,<br />
but might fail more often, due to error function used in the<br />
panotools optimizer, it tends to shrink the fov to 0. </p>
<p> rpyvb: Align pair by optimizing roll, pitch, yaw, field of view and<br />
&nbsp;<wbr>the&nbsp;<wbr>&#8220;b&#8221;&nbsp;<wbr>distortion parameter.&nbsp;<wbr>&nbsp;<wbr>Probably very fragile, just<br />
&nbsp;<wbr>implemented for testing. </p>
<p> auto: Use homography for images with hfov &lt; 65 degrees and rpy otherwise.</p>
<dt><code>&#8211;minmatches</code> &lt;int&gt;</p>
<dd> Minimum matches (default: 4)</p>
<dt><code>&#8211;sieve2width</code> &lt;int&gt;</p>
<dd> Sieve 2: Number of buckets on width (default: 5)</p>
<dt><code>&#8211;sieve2height</code> &lt;int&gt;</p>
<dd> Sieve 2: Number of buckets on height (default: 5)</p>
<dt><code>&#8211;sieve2size</code> &lt;int&gt;</p>
<dd> Sieve 2: Max points per bucket (default: 2) </p>
<p> Cpfind generates between minmatches and sieve2width * sieve2height * sieve2size control points between an image pair. (Default setting is between 4 and 50 (=5*5*2) control points per image pair.) If less then minmatches control points are found for a given image pairs these control points are disregarded and this image pair is considers as not connected. For narrow overlaps you can try to decrease minmatches, but this increases the risk of getting wrong control points.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;celesteRadius</code> &lt;int&gt;</p>
<dd> Radius for celeste (default 20)</p>
<dt><code>&#8211;celesteThreshold</code> &lt;double&gt;</p>
<dd> Threshold for celeste (default 0.5)</p>
<dt><code>&#8211;celeste</code></p>
<dd> Run celeste sky identification after loading images, this ignores all features associated with &#8216;clouds&#8217;.</p>
<dt><code>-p &lt;string</code>, <code>&#8211;keypath</code> &lt;string&gt;</p>
<dd> Path to cache keyfiles</p>
<dt><code>&#8211;clean</code></p>
<dd> Clean up cached keyfiles</p>
<dt><code>-c</code>, <code>&#8211;cache</code></p>
<dd> Caches keypoints to external file</p>
<dt><code>&#8211;kall</code></p>
<dd> Write keyfiles for all images</p>
<dt><code>-k</code> &lt;int&gt;, <code>&#8211;writekeyfile</code> &lt;int&gt;</p>
<dd> Write a keyfile for this image number (accepted multiple times)</p>
<dt><code>-o</code> &lt;string&gt;, <code>&#8211;output</code> &lt;string&gt;</p>
<dd> Output file, required</p>
<dt><code>-n</code> &lt;int&gt;, <code>&#8211;ncores</code> &lt;int&gt;</p>
<dd> Number of CPU/Cores (default:autodetect)</p>
<dt><code>-t</code>, <code>&#8211;test</code></p>
<dd> Enables test mode</p>
<dt><code>&#8211;fullscale</code></p>
<dd> Uses full scale image to detect keypoints (default:false)</p>
<dt><code>&#8211;sieve1width</code> &lt;int&gt;</p>
<dd> Sieve 1 : Number of buckets on width (default : 10)</p>
<dt><code>&#8211;sieve1height</code> &lt;int&gt;</p>
<dd> Sieve 1 : Number of buckets on height (default : 10)</p>
<dt><code>&#8211;sieve1size</code> &lt;int&gt;</p>
<dd> Sieve 1 : Max points per bucket (default : 100)</p>
<dt><code>&#8211;kdtreesteps</code> &lt;int&gt;</p>
<dd> KDTree : search steps (default : 200)</p>
<dt><code>&#8211;kdtreeseconddist</code> &lt;double&gt;</p>
<dd> KDTree : distance of 2nd match (default : 0.15)</p>
<dt><code>&#8211;multirow</code></p>
<dd> Enable heuristic multi row matching (default: off)</p>
<dt><code>&#8211;linearmatch</code></p>
<dd> Enable linear images matching (default : all pairs)</p>
<dt><code>&#8211;linearmatchlen</code> &lt;int&gt;</p>
<dd> Number of images to match in linear matching (default:1)</p>
<dt><code>&#8211;minmatches</code> &lt;int&gt;</p>
<dd> Minimum matches (default : 4)</p>
<dt><code>&#8211;ransaciter</code> &lt;int&gt;</p>
<dd> Ransac : iterations (default : 1000)</p>
<dt><code>&#8211;ransacdist</code> &lt;int&gt;</p>
<dd> Ransac : homography estimation distance threshold (pixels) (default : 25)</p>
<dt><code>&#8211;sieve2width</code> &lt;int&gt;</p>
<dd> Sieve 2 : Number of buckets on width (default : 5)</p>
<dt><code>&#8211;sieve2height</code> &lt;int&gt;</p>
<dd> Sieve 2 : Number of buckets on height (default : 5)</p>
<dt><code>&#8211;sieve2size</code> &lt;int&gt;</p>
<dd> Sieve 2 : Max points per bucket (default : 2)</p>
<dt><code>&#8212;</code>, <code>&#8211;ignore_rest</code></p>
<dd> Ignores the rest of the labeled arguments following this flag.</p>
<dt><code>&#8211;version</code></p>
<dd> Displays version information and exits.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Displays usage information and exits.</dl>
<h2>AUTHORS</h2>
<p> Anael Orlinski, Pablo d&#8217;Angelo, Antoine Deleforge, Thomas Modes </p>
<h2>Index</h2>
