---
title: "qwtinstall(3)"
name: "qwtinstall"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtinstall/"
description: "qwtinstall – Installing Qwt"
---

<p>qwtinstall &#8211; Installing Qwt</p>
<h2>Download</h2>
<p>Stable Qwt releases are available from the Qwt project page. </p>
<p> Qwt-6.1.1 consists of 4 files: </p>
<dl>
<dt>&bull;</p>
<dd>qwt-6.1.1.zip </p>
<p>&nbsp;<wbr>Zip file with the Qwt sources and the html documentation for Windows</p>
<dt>&bull;</p>
<dd>qwt-6.1.1.tar.bz2 </p>
<p>&nbsp;<wbr>Compressed tar file with the Qwt sources and the html documentation for UNIX systems&nbsp;<wbr>(&nbsp;<wbr>Linux, Mac, &#8230;&nbsp;<wbr>)</p>
<dt>&bull;</p>
<dd>qwt-6.1.1.pdf </p>
<p>&nbsp;<wbr>Qwt documentation as PDF document.</p>
<dt>&bull;</p>
<dd>qwt-6.1.1.qch </p>
<p>&nbsp;<wbr>Qwt documentation as Qt Compressed Help document, that can be loaded into the Qt Assistant or Creator. In the Qt Creator context sensitive help will be available like for Qt classes.</dl>
<p> Precompiled Qwt Designer plugins, that are compatible with some binary packages of the Qt Creator: </p>
<dl>
<dt>&bull;</p>
<dd>qwtdesigner-6.1.1-*.zip</dl>
<h2>Installing Qwt</h2>
<p>Beside headers, libraries and the html version of the class documentation a proper Qwt installation contains a Designer plugin and a Qwt features file for building applications using Qwt. </p>
<p> All files will be copied to an installation directory, that is configurable by editing qwtconfig.pri. Its default settings is: </p>
<dl>
<dt>&bull;</p>
<dd>Windows </p>
<p>&nbsp;<wbr>C:\Qwt-6.1.1</p>
<dt>&bull;</p>
<dd>Unix like systems </p>
<p>&nbsp;<wbr>/usr/local/qwt-6.1.1</dl>
<p> For the rest of the document this install path will be written as <i>${QWT_ROOT}</i> and needs to be replaced by the real path in all commands below. </p>
<p> It is not unlikely, to have more than one installation of Qwt on the same system. F.e for using the Qwt Designer plugin in the Qt Creator a version of Qwt is necessary with the same Qt and compiler combination, that had been used for building the Qt Creator ( see &#8216;Help-&gt;About Qt Creator &#8230;&#8217; ). </p>
<p> Installing Qwt is done in 3 steps, that are quite common on UNIX systems. </p>
<dl>
<dt>1.</p>
<dd>Configuration </p>
<p>&nbsp;<wbr>In the configuration step all parameters are set to control how to build and install Qwt</p>
<dt>2.</p>
<dd>Build </p>
<p>&nbsp;<wbr>In the build step binaries are built from the source files.</p>
<dt>3.</p>
<dd>Installation </p>
<p>&nbsp;<wbr>The installation copies and rearranges all files that are necessary to build Qwt applications to a target directory.</dl>
<p> The installation doesn&#8217;t modify the system beside copying files to a directory in a proper way. After removing build and installation directories the system is in the same state as it was before.</p>
<h3>Configuration</h3>
<p>Configuring Qwt has to be done by editing the Project files used for building: </p>
<dl>
<dt>&bull;</p>
<dd>qwtbuild.pri </p>
<p>&nbsp;<wbr>qwtbuild.pri contains settings for how to build Qwt. All settings of this file are only for building Qwt itself and doesn&#8217;t have an impact on how an application using Qwt is built. Usually its default settings doesn&#8217;t need to be modified.</p>
<dt>&bull;</p>
<dd>qwtconfig.pri </p>
<p>&nbsp;<wbr>qwtconfig.pri defines what modules of Qwt will be built and where to install them. qwtconfig.pri gets installed together with the Qwt features file qwt.prf and all its settings are known to project files for building Qwt applications.</dl>
<p> In qwtconfig.pri the meaning of each option is explained in detail &#8211; it&#8217;s worth reading it before running into problems later.</p>
<h3>Build and installation</h3>
<p>The Qt Creator is a graphical frontend for calling qmake/make and &#8211; technically &#8211; it could be used for building and installing Qwt. But as this way requires a lot more understanding of details the following step by step instructions are for the easier way using the command line.</p>
<h3>Unix-like systems</h3>
<p>The first step before creating the Makefile is to check that the correct version of qmake is used. F.e. on older Linux distribution you often find a Qt3 qmake and in the path. </p>
<p> The default setting of qmake is to generate a makefile that builds Qwt for the same environment where the version of qmake has been built for. So creating a makefile usually means something like: </p>
<pre>cd qwt-6.1.1
/usr/local/Qt-5.0.1/bin/qmake qwt.pro</pre>
<p>The generated Makefile includes all paths related to the chosen Qt version and the next step is: </p>
<pre>make</pre>
<p>&nbsp;<wbr>(&nbsp;<wbr>On multicore systems you can speed up building the Qwt libraries with running several jobs simultaneously: f.e.&nbsp;<wbr>&#8216;make -j4&#8217;&nbsp;<wbr>on a dual core.&nbsp;<wbr>) </p>
<p> Finally you have to install everything below the directories you have specified in qwtconfig.pri. Usually this is one of the system directories ( /usr/local, /opt, &#8230; ) where you don&#8217;t have write permission and then the installation needs to be done as root: </p>
<pre>sudo make install</pre>
<p>&nbsp;<wbr>(&nbsp;<wbr>On systems where sudo is not supported you can do the same with: su -c&nbsp;<wbr>&#8216;make install&#8217;&nbsp;<wbr>)</p>
<h3>Windows</h3>
<p>Qt packages offer a command line interface, that can be found in the Qt application menu: f.e &#8216;All Programs -&gt; Qt -&gt; Command Prompt&#8217;. It is not mandatory to use it, but probably the easiest way as it offers an environment, where everything is initialized for a version of Qt ( f.e qmake is in the PATH ). </p>
<p> Creating a makefile usually means something like: </p>
<pre>cd qwt-6.1.1
qmake qwt.pro</pre>
<p>The generated makefile includes all paths related to the chosen Qt version.</p>
<h3>MinGW</h3>
<p>For MinGW builds the name of the make tool is &#8216;mingw32-make&#8217; </p>
<pre>mingw32-make</pre>
<p>&nbsp;<wbr>(&nbsp;<wbr>On multicore systems you can speed up building the Qwt libraries with running several jobs simultaneously:&nbsp;<wbr>&#8216;mingw32-make -j&#8217;&nbsp;<wbr>) </p>
<p> Finally you have to install everything below the directories you have specified in qwtconfig.pri. </p>
<pre>mingw32-make install</pre>
<h3>Msvc</h3>
<p>For MSVC builds the name of the make tool is &#8216;nmake&#8217;. Alternatively it is possible to use &#8216;jom&#8217; ( <a rel="nofollow" href="http://qt-project.org/wiki/jom">http://qt-project.org/wiki/jom</a> ), that is usually included in a Qt Creator package. </p>
<pre>nmake</pre>
<p>Finally you have to install everything below the directories you have specified in qwtconfig.pri. </p>
<pre>nmake install</pre>
<h2>Qwt and the Qt tool chain</h2>
<h3>Designer plugin</h3>
<p>The Designer plugin and the corresponding Qwt library ( if the plugin has not been built self containing ) have to be compatible with Qt version of the application loading it ( usually the Qt Creator ) &#8211; what is often a different version of the Qt libraries you want to build your application with. F.e on Windows the Qt Creator is usually built with a MSVC compiler &#8211; even if included in a MinGW package ! </p>
<p> To help Qt Designer/Creator with locating the Qwt Designer plugin you have to set the environment variable QT_PLUGIN_PATH, modify qt.conf &#8211; or install the plugin to one of the application default paths. </p>
<p> The Qt documentation explains all options in detail: </p>
<dl>
<dt>&bull;</p>
<dd><a rel="nofollow" href="http://qt-project.org/doc/qt-5.0/qtdoc/deployment-plugins.html">http://qt-project.org/doc/qt-5.0/qtdoc/deployment-plugins.html</a></p>
<dt>&bull;</p>
<dd><a rel="nofollow" href="http://qt-project.org/doc/qtcreator-2.7/adding-plugins.html.">http://qt-project.org/doc/qtcreator-2.7/adding-plugins.html.</a></dl>
<p> F.e. on a Linux system you could add the following lines to .bashrc: </p>
<pre>QT_PLUGIN_PATH=&quot;${QWT_ROOT}/plugins:$QT_PLUGIN_PATH&quot;
export QT_PLUGIN_PATH</pre>
<p>When the plugin has not been built including the Qwt library ( see QwtDesignerSelfContained in qwtconfig.pri ) the Qt Designer/Creator also needs to locate the Qwt libraries. On Unix systems the path to the installed library is compiled into the plugin ( see rpath, ldd ), but on Windows the Qt Creator needs to be configured ( ( <code>Running a Qwt application</code> ) in the same way as for any application using Qwt. </p>
<p> In case of problems the diagnostics of Qt Creator and Designer are very limited ( usually none ), but setting the environment variable QT_DEBUG_PLUGINS might help. In the Qt Creator it is possible to check which plugins were loaded successfully and for certain problems it also lists those that were recognized but failed ( <i>Tools &gt; Form Editor &gt; About Qt Designer Plugins</i> ).</p>
<h3>Online Help</h3>
<p>The Qwt class documentation can be loaded into the Qt Creator: </p>
<dl>
<dt>&bull;</p>
<dd>open the settings dialog from the <i>Tools-&gt;Options</i> menu</p>
<dt>&bull;</p>
<dd>raise the tab &#8216;Help-&gt;Documentation&#8217;.</p>
<dt>&bull;</p>
<dd>press the <i>Add</i> button and select qwt-6.1.1.qch.</dl>
<p> Now the context sensitive help ( <i>F1</i> ) works for Qwt classes. </p>
<p> For browsing the documentation in the Qt Assistant: </p>
<dl>
<dt>&bull;</p>
<dd>open the settings dialog from the <i>Edit-&gt;Preferences</i> menu</p>
<dt>&bull;</p>
<dd>raise the tab <i>Documentation</i>.</p>
<dt>&bull;</p>
<dd>press the <i>Add</i> button and select qwt-6.1.1.qch.</dl>
<h2>Building a Qwt application</h2>
<p>All flags and settings that are necessary to compile and link an application using Qwt can be found in the file ${QWT_ROOT}/features/qwt.prf. </p>
<p> When using qmake it can included from the application project file in 2 different ways: </p>
<dl>
<dt>&bull;</p>
<dd>Adding Qwt as qmake feature </p>
<p>&nbsp;<wbr>When using the qmake feature mechanism you can bind a special version of qmake to a special installation of Qwt without having to add this dependency to the application project. How to add Qwt as feature is documented in the qmake docs.</dl>
<p> After adding Qwt as a feature f.e on Linux as a persistent property &#8230;. </p>
<pre>qmake -set QMAKEFEATURES ${QWT_ROOT}/features</pre>
<p>&nbsp;<wbr>.. the following line can be added to the application project file:&nbsp;<wbr> </p>
<pre>CONFIG += qwt</pre>
<dl>
<dt>&bull;</p>
<dd>Including qwt.prf in the application project file </p>
<p>&nbsp;<wbr>Instead of using qwt.prf as qmake feature it can be included from the application project file: </p>
</dl>
<pre>include ( ${QWT_ROOT}/features/qwt.prf )</pre>
<p>&nbsp;<wbr> </p>
<p>&nbsp;<wbr>The advantage of using a direct include is, that all settings of qwt.prf are known to the application project file&nbsp;<wbr>(&nbsp;<wbr>qmake features are included after the application project file has been parsed&nbsp;<wbr>)&nbsp;<wbr>and it can be implemented depending on &#8211; f.e. settings made in qwtconfig.pri. </p>
<p> On Unix platforms it is possible to link a runtime path into the executable, so that the location of the Qwt libraries can be found without having to configure a runtime environment:</p>
<dl>
<dt>&bull;</p>
<dd>QMAKE_LFLAGS_RPATH</p>
<dt>&bull;</p>
<dd>QMAKE_RPATH</p>
<dt>&bull;</p>
<dd>QMAKE_RPATHDIR</dl>
<h2>Running a Qwt application</h2>
<p>When using Qwt as shared library ( DLL ) the dynamic linker has to find it according to the rules of the operating system.</p>
<h3>Windows</h3>
<p>The only reasonable way to configure the runtime environment &#8211; without having to copy the Qwt libraries around &#8211; is to modify the PATH variable. F.e. this could be done by adding the following line to some batch file: </p>
<pre>set PATH=%PATH%;${QWT_ROOT}<HR></pre>
<h3>GNU/Linux</h3>
<p>Read the documentation about: </p>
<dl>
<dt>&bull;</p>
<dd><i>ldconfig</i></p>
<dt>&bull;</p>
<dd><i>/etc/ld.so.conf</i></p>
<dt>&bull;</p>
<dd><i>LD_LIBRARY_PATH</i></dl>
<p> Using the <i>ldd</i> command a configuration can be tested.</p>
