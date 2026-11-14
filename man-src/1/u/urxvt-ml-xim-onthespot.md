---
title: "urxvt-ml-xim-onthespot(1)"
name: "urxvt-ml-xim-onthespot"
section: "1"
letter: "u"
url: "/docs/linux/man/1-urxvt-ml-xim-onthespot/"
---

<h2 class="name">NAME</h2>
 

 xim-onthespot - implement XIM &quot;on-the-spot&quot; behaviour 

<h2>DESCRIPTION</h2>

 This perl extension implements OnTheSpot editing. It does not work perfectly, and some input methods don't seem to work well with OnTheSpot editing in general, but it seems to work at least for <font SIZE="-1">SCIM</font> and kinput2. 

 You enable it by specifying this extension and a preedit style of <tt>&quot;OnTheSpot&quot;</tt>, i.e.: 

 <pre>
   urxvt -pt OnTheSpot -pe xim-onthespot
</pre> 

<h2>Index</h2>


