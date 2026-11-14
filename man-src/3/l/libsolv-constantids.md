---
title: "libsolv-constantids(3)"
name: "libsolv-constantids"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libsolv-constantids/"
description: "libsolv-constantids – fixed Ids for often used strings"
---

<h2 class="name">NAME</h2>
<p> libsolv-constantids &#8211; fixed Ids for often used strings </p>
<h2>DESCRIPTION</h2>
<p> Constant Ids are Ids of strings that are often needed. They are defined to ease programming and reduce the number of pool_str2id calls. The constant Ids are part of the binary ABI of libsolv, a minor version update will only add new constants and not change existing Ids to maintain compatible. The on-disk solv format works does not use the fixed Ids, but instead references the strings, so solv files can still be read when the ABI is broken.</p>
<h2>SPECIAL STRINGS</h2>
<p> <code>ID_EMPTY &quot;&quot;</code></p>
<dl>
<dt>
<dd> The empty string. It will always have Id 1.</dl>
<p> <code>SYSTEM_SYSTEM &quot;system:system&quot;</code></p>
<dl>
<dt>
<dd> The name of the always installed &quot;system&quot; solvable.</dl>
<h2>SOLVABLE ATTRIBUTES</h2>
<p> These are Ids for keyname of attributes. They can be used in the lookup and storage functions to select the correct attribute in the solvable. The descriptions below describe the intended semantics of the values stored in the attribute with the keyname. </p>
<p> <code>SOLVABLE_NAME &quot;solvable:name&quot;</code></p>
<dl>
<dt>
<dd> The name of the package.</dl>
<p> <code>SOLVABLE_ARCH &quot;solvable:arch&quot;</code></p>
<dl>
<dt>
<dd> The architecture of the package. See the Solvable Architecture section for predefined architecture Id values.</dl>
<p> <code>SOLVABLE_EVR &quot;solvable:evr&quot;</code></p>
<dl>
<dt>
<dd> The version of the package. It usually consists of some combination of the Epoch, the Version, and the Release of the solvable.</dl>
<p> <code>SOLVABLE_VENDOR &quot;solvable:vendor&quot;</code></p>
<dl>
<dt>
<dd> A vendor string. Usually the company or group that created the binary package.</dl>
<p> <code>SOLVABLE_PROVIDES &quot;solvable:provides&quot;</code></p>
<dl>
<dt>
<dd> Stores an array of dependency Ids that describe the capabilities that the package provides.</dl>
<p> <code>SOLVABLE_OBSOLETES &quot;solvable:obsoletes&quot;</code></p>
<dl>
<dt>
<dd> Stores an array of dependency Ids that describe the packages that this package replaces.</dl>
<p> <code>SOLVABLE_CONFLICTS &quot;solvable:conflicts&quot;</code></p>
<dl>
<dt>
<dd> Stores an array of dependency Ids that describe the capabilities that this package conflicts with, i.e. that can&#8217;t be installed together with this package.</dl>
<p> <code>SOLVABLE_REQUIRES &quot;solvable:requires&quot;</code></p>
<dl>
<dt>
<dd> Stores an array of dependency Ids that describe the capabilities that also must be installed when this package is installed.</dl>
<p> <code>SOLVABLE_RECOMMENDS &quot;solvable:recommends&quot;</code></p>
<dl>
<dt>
<dd> Stores an array of dependency Ids that describe the capabilities that also should be installed when this package is installed. It&#8217;s not an error if not all capabilities can be met.</dl>
<p> <code>SOLVABLE_SUGGESTS &quot;solvable:suggests&quot;</code></p>
<dl>
<dt>
<dd> Stores an array of dependency Ids that describe the capabilities that also useful to have installed when this package is installed. This is intended to provide a hint to the user about other packages.</dl>
<p> <code>SOLVABLE_SUPPLEMENTS &quot;solvable:supplements&quot;</code></p>
<dl>
<dt>
<dd> Stores an array of dependency Ids that define that this package should be installed if one of the capabilities is met. This is like the recommends attribute, but works in the reverse way.</dl>
<p> <code>SOLVABLE_ENHANCES &quot;solvable:enhances&quot;</code></p>
<dl>
<dt>
<dd> Stores an array of dependency Ids that define that this package is useful to have installed if one of the capabilities is met. This is like the suggests attribute, but works in the reverse way.</dl>
<p> <code>SOLVABLE_SUMMARY &quot;solvable:summary&quot;</code></p>
<dl>
<dt>
<dd> The summary should be a short string without any newlines that describes what a package does.</dl>
<p> <code>SOLVABLE_DESCRIPTION &quot;solvable:description&quot;</code></p>
<dl>
<dt>
<dd> The description should be a more verbose description about what a package does. It may consist of multiple lines.</dl>
<p> <code>SOLVABLE_DISTRIBUTION &quot;solvable:distribution&quot;</code></p>
<dl>
<dt>
<dd> The distribution is a short string that describes the OS and OS version this package is built for.</dl>
<p> <code>SOLVABLE_AUTHORS &quot;solvable:authors&quot;</code></p>
<dl>
<dt>
<dd> A list of authors of this package. This attribute was used in SUSE packages.</dl>
<p> <code>SOLVABLE_PACKAGER &quot;solvable:packager&quot;</code></p>
<dl>
<dt>
<dd> The person who created the binary package, see also the vendor attribute.</dl>
<p> <code>SOLVABLE_GROUP &quot;solvable:group&quot;</code></p>
<dl>
<dt>
<dd> The package group that this package belongs to. See also the keywords attribute.</dl>
<p> <code>SOLVABLE_URL &quot;solvable:url&quot;</code></p>
<dl>
<dt>
<dd> An URL that points to more information about the package.</dl>
<p> <code>SOLVABLE_KEYWORDS &quot;solvable:keywords&quot;</code></p>
<dl>
<dt>
<dd> list of keyword string IDs used for tagging this package.</dl>
<p> <code>SOLVABLE_LICENSE &quot;solvable:license&quot;</code></p>
<dl>
<dt>
<dd> The license(s) of this package.</dl>
<p> <code>SOLVABLE_BUILDTIME &quot;solvable:buildtime&quot;</code></p>
<dl>
<dt>
<dd> The seconds since the unix epoch when the binary package was created.</dl>
<p> <code>SOLVABLE_BUILDHOST &quot;solvable:buildhost&quot;</code></p>
<dl>
<dt>
<dd> The name of the host on which the binary package was created.</dl>
<p> <code>SOLVABLE_EULA &quot;solvable:eula&quot;</code></p>
<dl>
<dt>
<dd> If this attribute is present the user should be asked to accept the end user license agreement before the package gets installed.</dl>
<p> <code>SOLVABLE_CPEID &quot;solvable:cpeid&quot;</code></p>
<dl>
<dt>
<dd> A Common Platform Enumeration string describes the platform this package is intended for. See also the distribution attribute.</dl>
<p> <code>SOLVABLE_MESSAGEINS &quot;solvable:messageins&quot;</code></p>
<dl>
<dt>
<dd> A message that should be displayed to the user when the package gets installed.</dl>
<p> <code>SOLVABLE_MESSAGEDEL &quot;solvable:messagedel&quot;</code></p>
<dl>
<dt>
<dd> A message that should be displayed to the user when the package gets erased.</dl>
<p> <code>SOLVABLE_INSTALLSIZE &quot;solvable:installsize&quot;</code></p>
<dl>
<dt>
<dd> The disk space in bytes needed when installing the package.</dl>
<p> <code>SOLVABLE_DISKUSAGE &quot;solvable:diskusage&quot;</code></p>
<dl>
<dt>
<dd> A SUSE extension that stores for each directory the needed amount of disk space in kilobytes and inodes.</dl>
<p> <code>SOLVABLE_FILELIST &quot;solvable:filelist&quot;</code></p>
<dl>
<dt>
<dd> A list of files that the package contains.</dl>
<p> <code>SOLVABLE_INSTALLTIME &quot;solvable:installtime&quot;</code></p>
<dl>
<dt>
<dd> The seconds since the unix epoch when the binary package was installed on the system.</dl>
<p> <code>SOLVABLE_MEDIADIR &quot;solvable:mediadir&quot;</code></p>
<dl>
<dt>
<dd> The directory on the repository that contains the package. If this attribute is set to void, the package architecture is used as directory.</dl>
<p> <code>SOLVABLE_MEDIAFILE &quot;solvable:mediafile&quot;</code></p>
<dl>
<dt>
<dd> The filename on the repository that contains the package. If this attribute is set to void, the canonical file name of the package is used (i.e. a combination of the name, version, architecture).</dl>
<p> <code>SOLVABLE_MEDIANR &quot;solvable:medianr&quot;</code></p>
<dl>
<dt>
<dd> The media number. This is an integer describing on which of a multi-part media set this package is on.</dl>
<p> <code>SOLVABLE_MEDIABASE &quot;solvable:mediabase&quot;</code></p>
<dl>
<dt>
<dd> This attribute can be used to overwrite the repositories base url.</dl>
<p> <code>SOLVABLE_DOWNLOADSIZE &quot;solvable:downloadsize&quot;</code></p>
<dl>
<dt>
<dd> The size of the binary package in bytes.</dl>
<p> <code>SOLVABLE_SOURCEARCH &quot;solvable:sourcearch&quot;</code></p>
<dl>
<dt>
<dd> The architecture of the source package that this package belongs to.</dl>
<p> <code>SOLVABLE_SOURCENAME &quot;solvable:sourcename&quot;</code></p>
<dl>
<dt>
<dd> The name of the source package that this package belongs to. If set to void, the package name attribute is used instead.</dl>
<p> <code>SOLVABLE_SOURCEEVR &quot;solvable:sourceevr&quot;</code></p>
<dl>
<dt>
<dd> The version of the source package that this package belongs to. If set to void, the package version attribute is used instead.</dl>
<p> <code>SOLVABLE_TRIGGERS &quot;solvable:triggers&quot;</code></p>
<dl>
<dt>
<dd> A list of package triggers for this package. Used in the transaction ordering code.</dl>
<p> <code>SOLVABLE_CHECKSUM &quot;solvable:checksum&quot;</code></p>
<dl>
<dt>
<dd> The checksum of the binary package. See the Data Types section for a list of supported algorithms.</dl>
<p> <code>SOLVABLE_PKGID &quot;solvable:pkgid&quot;</code></p>
<dl>
<dt>
<dd> A string identifying a package. For rpm packages, this is the md5sum over the package header and the payload.</dl>
<p> <code>SOLVABLE_HDRID &quot;solvable:hdrid&quot;</code></p>
<dl>
<dt>
<dd> A string identifying a package. For rpm packages, this is the sha1sum over just the package header.</dl>
<p> <code>SOLVABLE_LEADSIGID &quot;solvable:leadsigid&quot;</code></p>
<dl>
<dt>
<dd> A string identifying the signature part of a package. For rpm packages, this is the md5sum from the start of the file up to the package header (i.e. it includes the lead, the signature header, and the padding).</dl>
<p> <code>SOLVABLE_HEADEREND &quot;solvable:headerend&quot;</code></p>
<dl>
<dt>
<dd> The offset of the payload in rpm binary packages. You can use this information to download just the header if you want to display information not included in the repository metadata.</dl>
<p> <code>SOLVABLE_CHANGELOG &quot;solvable:changelog&quot;</code></p>
<dl>
<dt>
<dd> The array containing all the changelog structures.</dl>
<p> <code>SOLVABLE_CHANGELOG_AUTHOR &quot;solvable:changelog:author&quot;</code></p>
<dl>
<dt>
<dd> The author of a changelog entry.</dl>
<p> <code>SOLVABLE_CHANGELOG_TIME &quot;solvable:changelog:time&quot;</code></p>
<dl>
<dt>
<dd> The seconds since the unix epoch when the changelog entry was written.</dl>
<p> <code>SOLVABLE_CHANGELOG_TEXT &quot;solvable:changelog:text&quot;</code></p>
<dl>
<dt>
<dd> The text of a changelog entry.</dl>
<h2>SPECIAL SOLVABLE ATTRIBUTES</h2>
<p> <code>RPM_RPMDBID &quot;rpm:dbid&quot;</code></p>
<dl>
<dt>
<dd> The rpm database id of this (installed) package. Usually a small integer number.</dl>
<p> <code>SOLVABLE_PATCHCATEGORY &quot;solvable:patchcategory&quot;</code></p>
<dl>
<dt>
<dd> The category field for patch solvables. Should be named &#8220;update:category&#8221; instead.</dl>
<p> <code>UPDATE_REBOOT &quot;update:reboot&quot;</code></p>
<dl>
<dt>
<dd> If this attribute is present the system should be rebooted after the update is installed.</dl>
<p> <code>UPDATE_RESTART &quot;update:restart&quot;</code></p>
<dl>
<dt>
<dd> If this attribute is present the software manager should be run again after the update is installed.</dl>
<p> <code>UPDATE_RELOGIN &quot;update:relogin&quot;</code></p>
<dl>
<dt>
<dd> If this attribute is present the user should log off and on again after the update is installed.</dl>
<p> <code>UPDATE_MESSAGE &quot;update:message&quot;</code></p>
<dl>
<dt>
<dd> A message that should be shown to the user to warn him about anything non-standard.</dl>
<p> <code>UPDATE_SEVERITY &quot;update:severity&quot;</code></p>
<dl>
<dt>
<dd> The severity of the update.</dl>
<p> <code>UPDATE_RIGHTS &quot;update:rights&quot;</code></p>
<dl>
<dt>
<dd> Any legal or other rights of the update.</dl>
<p> <code>UPDATE_COLLECTION &quot;update:collection&quot;</code></p>
<dl>
<dt>
<dd> The array containing the package list of the update.</dl>
<p> <code>UPDATE_COLLECTION_NAME &quot;update:collection:name&quot;</code></p>
<dl>
<dt>
<dd> The name of the updated package.</dl>
<p> <code>UPDATE_COLLECTION_EVR &quot;update:collection:evr&quot;</code></p>
<dl>
<dt>
<dd> The version of the updated package.</dl>
<p> <code>UPDATE_COLLECTION_ARCH &quot;update:collection:arch&quot;</code></p>
<dl>
<dt>
<dd> The architecture of the updated package.</dl>
<p> <code>UPDATE_COLLECTION_FILENAME &quot;update:collection:filename&quot;</code></p>
<dl>
<dt>
<dd> The file name of the updated package.</dl>
<p> <code>UPDATE_REFERENCE &quot;update:reference&quot;</code></p>
<dl>
<dt>
<dd> The array containing the reference list of the update.</dl>
<p> <code>UPDATE_REFERENCE_TYPE &quot;update:reference:type&quot;</code></p>
<dl>
<dt>
<dd> The type of the reference, e.g. bugzilla.</dl>
<p> <code>UPDATE_REFERENCE_href &quot;update:reference:href&quot;</code></p>
<dl>
<dt>
<dd> The URL of the reference.</dl>
<p> <code>UPDATE_REFERENCE_ID &quot;update:reference:id&quot;</code></p>
<dl>
<dt>
<dd> The identification string of the reference, e.g. the bug number.</dl>
<p> <code>UPDATE_REFERENCE_TITLE &quot;update:reference:title&quot;</code></p>
<dl>
<dt>
<dd> The title of the reference, e.g. the bug summary.</dl>
<p> <code>PRODUCT_REFERENCEFILE &quot;product:referencefile&quot;</code></p>
<dl>
<dt>
<dd> The basename of the product file in the package.</dl>
<p> <code>PRODUCT_SHORTLABEL &quot;product:shortlabel&quot;</code></p>
<dl>
<dt>
<dd> An identification string of the product.</dl>
<p> <code>PRODUCT_DISTPRODUCT &quot;product:distproduct&quot;</code></p>
<dl>
<dt>
<dd> Obsolete, do not use. Was a SUSE Code-10 product name.</dl>
<p> <code>PRODUCT_DISTVERSION &quot;product:distversion&quot;</code></p>
<dl>
<dt>
<dd> Obsolete, do not use. Was a SUSE Code-10 product version.</dl>
<p> <code>PRODUCT_TYPE &quot;product:type&quot;</code></p>
<dl>
<dt>
<dd> The type of the product, e.g. &#8220;base&#8221;.</dl>
<p> <code>PRODUCT_URL &quot;product:url&quot;</code></p>
<dl>
<dt>
<dd> An array of product URLs.</dl>
<p> <code>PRODUCT_URL_TYPE &quot;product:url:type&quot;</code></p>
<dl>
<dt>
<dd> An array of product URL types.</dl>
<p> <code>PRODUCT_FLAGS &quot;product:flags&quot;</code></p>
<dl>
<dt>
<dd> An array of product flags.</dl>
<p> <code>PRODUCT_PRODUCTLINE &quot;product:productline&quot;</code></p>
<dl>
<dt>
<dd> A product line string used for product registering.</dl>
<p> <code>PRODUCT_REGISTER_TARGET &quot;product:regtarget&quot;</code></p>
<dl>
<dt>
<dd> A target for product registering.</dl>
<p> <code>PRODUCT_REGISTER_RELEASE &quot;product:regrelease&quot;</code></p>
<dl>
<dt>
<dd> A release string for product registering.</dl>
<p> <code>PUBKEY_KEYID &quot;pubkey:keyid&quot;</code></p>
<dl>
<dt>
<dd> The keyid of a pubkey, consisting of 8 bytes in hex.</dl>
<p> <code>PUBKEY_FINGERPRINT &quot;pubkey:fingerprint&quot;</code></p>
<dl>
<dt>
<dd> The fingerprint of a pubkey, usually a sha1sum in hex. Old V3 RSA keys use a md5sum instead.</dl>
<p> <code>PUBKEY_EXPIRES &quot;pubkey:expires&quot;</code></p>
<dl>
<dt>
<dd> The seconds since the unix epoch when the pubkey expires.</dl>
<p> <code>PUBKEY_SUBKEYOF &quot;pubkey:subkeyof&quot;</code></p>
<dl>
<dt>
<dd> The keyid of the master pubkey for subkeys.</dl>
<p> <code>PUBKEY_DATA &quot;pubkey:data&quot;</code></p>
<dl>
<dt>
<dd> The MPI data of the pubkey.</dl>
<p> <code>SOLVABLE_ISVISIBLE &quot;solvable:isvisible&quot;</code></p>
<dl>
<dt>
<dd> An attribute describing if the package should be listed to the user or not. Used for SUSE patterns.</dl>
<p> <code>SOLVABLE_CATEGORY &quot;solvable:category&quot;</code></p>
<dl>
<dt>
<dd> The category of a pattern.</dl>
<p> <code>SOLVABLE_INCLUDES &quot;solvable:includes&quot;</code></p>
<dl>
<dt>
<dd> A list of other patterns that this pattern includes.</dl>
<p> <code>SOLVABLE_EXTENDS &quot;solvable:extends&quot;</code></p>
<dl>
<dt>
<dd> A list of other patterns that this pattern extends.</dl>
<p> <code>SOLVABLE_ICON &quot;solvable:icon&quot;</code></p>
<dl>
<dt>
<dd> The icon name of a pattern.</dl>
<p> <code>SOLVABLE_ORDER &quot;solvable:order&quot;</code></p>
<dl>
<dt>
<dd> An ordering clue of a pattern.</dl>
<p> <code>SUSETAGS_SHARE_NAME &quot;susetags:share:name&quot;</code></p>
<dl>
<dt>
<dd> Internal attribute to implement susetags shared records. Holds the name of the solvable used for sharing attributes.</dl>
<p> <code>SUSETAGS_SHARE_EVR &quot;susetags:share:evr&quot;</code></p>
<dl>
<dt>
<dd> Internal attribute to implement susetags shared records. Holds the version of the solvable used for sharing attributes.</dl>
<p> <code>SUSETAGS_SHARE_ARCH &quot;susetags:share:arch&quot;</code></p>
<dl>
<dt>
<dd> Internal attribute to implement susetags shared records. Holds the architecture of the solvable used for sharing attributes.</dl>
<h2>SOLVABLE ARCHITECTURES</h2>
<p> Predefined architecture values for commonly used architectures. </p>
<p> <code>ARCH_SRC &quot;src&quot;</code></p>
<dl>
<dt>
<dd> Used for binary packages that contain the package sources.</dl>
<p> <code>ARCH_NOSRC &quot;nosrc&quot;</code></p>
<dl>
<dt>
<dd> Used for binary packages that contain some of the package sources, but not all files (because of restrictions).</dl>
<p> <code>ARCH_NOARCH &quot;noarch&quot;</code></p>
<dl>
<dt>
<dd> This package can be installed on any architecture. Used for rpm.</dl>
<p> <code>ARCH_ALL &quot;all&quot;</code></p>
<dl>
<dt>
<dd> This package can be installed on any architecture. Used for Debian.</dl>
<p> <code>ARCH_ANY &quot;any&quot;</code></p>
<dl>
<dt>
<dd> This package can be installed on any architecture. Used for Archlinux and Haiku.</dl>
<h2>DEPENDENCY IDS</h2>
<p> Namespaces are special modifiers that change the meaning of a dependency. Namespace dependencies are created with the REL_NAMESPACE flag. To make custom namespaces work you have to implement a namespace callback function. </p>
<p> The dependency markers partition the dependency array in two parts with different semantics. </p>
<p> <code>NAMESPACE_MODALIAS &quot;namespace:modalias&quot;</code></p>
<dl>
<dt>
<dd> The dependency is a special modalias dependency that matches installed hardware.</dl>
<p> <code>NAMESPACE_SPLITPROVIDES &quot;namespace:splitprovides&quot;</code></p>
<dl>
<dt>
<dd> The dependency is a special splitprovides dependency used to implement updates that include a package split. A splitprovides dependency contains a filename and a package name, it is matched if a package with the provided package name is installed that contains the filename. This namespace is implemented in libsolv, so you do not need a callback.</dl>
<p> <code>NAMESPACE_LANGUAGE &quot;namespace:language&quot;</code></p>
<dl>
<dt>
<dd> The dependency describes a language. The callback should return true if the language was selected by the user.</dl>
<p> <code>NAMESPACE_FILESYSTEM &quot;namespace:filesystem&quot;</code></p>
<dl>
<dt>
<dd> The dependency describes a filesystem. The callback should return true if the filesystem is needed.</dl>
<p> <code>NAMESPACE_OTHERPROVIDERS &quot;namespace:otherproviders&quot;</code></p>
<dl>
<dt>
<dd> This is a hack to allow self-conflicting packages. It is not needed with current rpm version, so do not use this namespace.</dl>
<p> <code>SOLVABLE_PREREQMARKER &quot;solvable:prereqmarker&quot;</code></p>
<dl>
<dt>
<dd> This marker partitions the normal require dependencies from the prerequires. It is not needed for dependency solving, but it is used by the transaction ordering algorithm when a dependency cycle needs to be broken (non-prereq deps get broken first).</dl>
<p> <code>SOLVABLE_FILEMARKER &quot;solvable:filemarker&quot;</code></p>
<dl>
<dt>
<dd> This marker partitions the package provides dependencies from the synthetic file provides dependencies added by pool_addfileprovides().</dl>
<h2>DATA TYPES</h2>
<p> Each attribute data is stored with a type, so that the lookup functions know how to interpret the data. The following types are available: </p>
<p> <code>REPOKEY_TYPE_VOID &quot;repokey:type:void&quot;</code></p>
<dl>
<dt>
<dd> No data is stored with this attribute. Thus you can only test if the attribute exists or not. Useful to store boolean values.</dl>
<p> <code>REPOKEY_TYPE_CONSTANT &quot;repokey:type:constant&quot;</code></p>
<dl>
<dt>
<dd> The data is a constant 32bit number. The number is stored in the key area, so using it does not cost extra storage space (but you need the extra key space).</dl>
<p> <code>REPOKEY_TYPE_CONSTANTID &quot;repokey:type:constantid&quot;</code></p>
<dl>
<dt>
<dd> The data is a constant Id. The Id is stored in the key area, so using it does not cost extra storage space (but you need the extra key space).</dl>
<p> <code>REPOKEY_TYPE_ID &quot;repokey:type:id&quot;</code></p>
<dl>
<dt>
<dd> The data is an Id.</dl>
<p> <code>REPOKEY_TYPE_NUM &quot;repokey:type:num&quot;</code></p>
<dl>
<dt>
<dd> The data is an unsigned 64bit number.</dl>
<p> <code>REPOKEY_TYPE_U32 &quot;repokey:type:num32&quot;</code></p>
<dl>
<dt>
<dd> The data is an unsigned 32bit number. Obsolete, do not use.</dl>
<p> <code>REPOKEY_TYPE_DIR &quot;repokey:type:dir&quot;</code></p>
<dl>
<dt>
<dd> The data is an Id of a directory.</dl>
<p> <code>REPOKEY_TYPE_STR &quot;repokey:type:str&quot;</code></p>
<dl>
<dt>
<dd> The data is a regular string.</dl>
<p> <code>REPOKEY_TYPE_BINARY &quot;repokey:type:binary&quot;</code></p>
<dl>
<dt>
<dd> The data is a binary blob.</dl>
<p> <code>REPOKEY_TYPE_IDARRAY &quot;repokey:type:idarray&quot;</code></p>
<dl>
<dt>
<dd> The data is an array of non-zero Ids.</dl>
<p> <code>REPOKEY_TYPE_REL_IDARRAY &quot;repokey:type:relidarray&quot;</code></p>
<dl>
<dt>
<dd> The data is an array of non-zero Ids ordered so that it needs less space.</dl>
<p> <code>REPOKEY_TYPE_DIRSTRARRAY &quot;repokey:type:dirstrarray&quot;</code></p>
<dl>
<dt>
<dd> The data is a tuple consisting of a directory Id and a basename. Used to store file names.</dl>
<p> <code>REPOKEY_TYPE_DIRNUMNUMARRAY &quot;repokey:type:dirnumnumarray&quot;</code></p>
<dl>
<dt>
<dd> The data is a triple consisting of a directory Id and two 32bit unsigned integers. Used to store disk usage information.</dl>
<p> <code>REPOKEY_TYPE_MD5 &quot;repokey:type:md5&quot;</code></p>
<dl>
<dt>
<dd> The data is a binary md5sum.</dl>
<p> <code>REPOKEY_TYPE_SHA1 &quot;repokey:type:sha1&quot;</code></p>
<dl>
<dt>
<dd> The data is a binary sha1sum.</dl>
<p> <code>REPOKEY_TYPE_SHA256 &quot;repokey:type:sha256&quot;</code></p>
<dl>
<dt>
<dd> The data is a binary sha256sum.</dl>
<p> <code>REPOKEY_TYPE_FIXARRAY &quot;repokey:type:fixarray&quot;</code></p>
<dl>
<dt>
<dd> The data is an array of structures that have all the same layout (i.e. the same keynames and keytypes in the same order).</dl>
<p> <code>REPOKEY_TYPE_FLEXARRAY &quot;repokey:type:flexarray&quot;</code></p>
<dl>
<dt>
<dd> The data is an array of structures that have a different layout.</dl>
<p> <code>REPOKEY_TYPE_DELETED &quot;repokey:type:deleted&quot;</code></p>
<dl>
<dt>
<dd> The data does not exist. Used to mark an attribute that was deleted.</dl>
<h2>REPOSITORY METADATA</h2>
<p> This attributes contain meta information about the repository. </p>
<p> <code>REPOSITORY_SOLVABLES &quot;repository:solvables&quot;</code></p>
<dl>
<dt>
<dd> This attribute holds the array including all of the solvables. It is only used in the on-disk solv files, internally the solvables are stored in the pool&#8217;s solvable array for fast access.</dl>
<p> <code>REPOSITORY_DELTAINFO &quot;repository:deltainfo&quot;</code></p>
<dl>
<dt>
<dd> This attribute holds the array including all of the delta packages.</dl>
<p> <code>REPOSITORY_EXTERNAL &quot;repository:external&quot;</code></p>
<dl>
<dt>
<dd> This attribute holds the array including all of the data to construct stub repodata areas to support on-demand loading of metadata.</dl>
<p> <code>REPOSITORY_KEYS &quot;repository:keys&quot;</code></p>
<dl>
<dt>
<dd> This should really be named &quot;repository:external:keys&quot;, it contains an array if Ids that consists of (keyname, keytype) pairs that describe the keys of the stub.</dl>
<p> <code>REPOSITORY_LOCATION &quot;repository:location&quot;</code></p>
<dl>
<dt>
<dd> This is used to provide a file name in the stub.</dl>
<p> <code>REPOSITORY_ADDEDFILEPROVIDES &quot;repository:addedfileprovides&quot;</code></p>
<dl>
<dt>
<dd> This attribute holds an array of filename Ids, that tell the library, that all of the Ids were already added to the solvable provides.</dl>
<p> <code>REPOSITORY_RPMDBCOOKIE &quot;repository:rpmdbcookie&quot;</code></p>
<dl>
<dt>
<dd> An attribute that stores a sha256sum over the file stats of the Packages database. It&#8217;s used to detect rebuilds of the database, as in that case the database Ids of every package are newly distributed.</dl>
<p> <code>REPOSITORY_TIMESTAMP &quot;repository:timestamp&quot;</code></p>
<dl>
<dt>
<dd> The seconds since the unix epoch when the repository was created.</dl>
<p> <code>REPOSITORY_EXPIRE &quot;repository:expire&quot;</code></p>
<dl>
<dt>
<dd> The seconds after the timestamp when the repository will expire.</dl>
<p> <code>REPOSITORY_UPDATES &quot;repository:updates&quot;</code></p>
<dl>
<dt>
<dd> An array of structures describing what this repository updates.</dl>
<p> <code>REPOSITORY_DISTROS &quot;repository:distros&quot;</code></p>
<dl>
<dt>
<dd> Also an array of structures describing what this repository updates. Seems to be the newer name of REPOSITORY_UPDATES.</dl>
<p> <code>REPOSITORY_PRODUCT_LABEL &quot;repository:product:label&quot;</code></p>
<dl>
<dt>
<dd> Should really be called &quot;repository:updates:label&quot;. What distribution is updated with this repository.</dl>
<p> <code>REPOSITORY_PRODUCT_CPEID &quot;repository:product:cpeid&quot;</code></p>
<dl>
<dt>
<dd> The cpeid of the platform updated by this repository. Is both used in REPOSITORY_UPDATES and REPOSITORY_DISTROS to maximize confusion.</dl>
<p> <code>REPOSITORY_REPOID &quot;repository:repoid&quot;</code></p>
<dl>
<dt>
<dd> An array of Id strings describing keywords/tags about the repository itself.</dl>
<p> <code>REPOSITORY_KEYWORDS &quot;repository:keywords&quot;</code></p>
<dl>
<dt>
<dd> An array of Id strings describing keywords/tags about the content of the repository.</dl>
<p> <code>REPOSITORY_REVISION &quot;repository:revision&quot;</code></p>
<dl>
<dt>
<dd> An arbitrary string describing the revision of the repository.</dl>
<p> <code>REPOSITORY_TOOLVERSION &quot;repository:toolversion&quot;</code></p>
<dl>
<dt>
<dd> Some string describing somewhat the version of libsolv used to create the solv file.</dl>
<h2>REPOSITORY METADATA FOR SUSETAGS REPOS</h2>
<p> Attributes describing repository files in a susetags repository. <code>SUSETAGS_DATADIR &quot;susetags:datadir&quot;</code>:: The directory that contains the packages. </p>
<p> <code>SUSETAGS_DESCRDIR &quot;susetags:descrdir&quot;</code></p>
<dl>
<dt>
<dd> The directory that contains the repository file resources.</dl>
<p> <code>SUSETAGS_DEFAULTVENDOR &quot;susetags:defaultvendor&quot;</code></p>
<dl>
<dt>
<dd> The default vendor used when a package does not specify a vendor.</dl>
<p> <code>SUSETAGS_FILE &quot;susetags:file&quot;</code></p>
<dl>
<dt>
<dd> An array of file resources of the repository.</dl>
<p> <code>SUSETAGS_FILE_NAME &quot;susetags:file:name&quot;</code></p>
<dl>
<dt>
<dd> The filename of the resource.</dl>
<p> <code>SUSETAGS_FILE_TYPE &quot;susetags:file:type&quot;</code></p>
<dl>
<dt>
<dd> The type of the resource, e.g. &#8220;META&#8221;.</dl>
<p> <code>SUSETAGS_FILE_CHECKSUM &quot;susetags:file:checksum&quot;</code></p>
<dl>
<dt>
<dd> The file checksum of the resource.</dl>
<h2>REPOSITORY METADATA FOR RPMMD REPOS</h2>
<p> <code>REPOSITORY_REPOMD &quot;repository:repomd&quot;</code></p>
<dl>
<dt>
<dd> An array of file resources of the repository.</dl>
<p> <code>REPOSITORY_REPOMD_TYPE &quot;repository:repomd:type&quot;</code></p>
<dl>
<dt>
<dd> The type of the resource, e.g. &#8220;primary&#8221;.</dl>
<p> <code>REPOSITORY_REPOMD_LOCATION &quot;repository:repomd:location&quot;</code></p>
<dl>
<dt>
<dd> The location (aka filename) of the resource</dl>
<p> <code>REPOSITORY_REPOMD_TIMESTAMP &quot;repository:repomd:timestamp&quot;</code></p>
<dl>
<dt>
<dd> The seconds since the unix epoch when the resource was created.</dl>
<p> <code>REPOSITORY_REPOMD_CHECKSUM &quot;repository:repomd:checksum&quot;</code></p>
<dl>
<dt>
<dd> The file checksum of the resource.</dl>
<p> <code>REPOSITORY_REPOMD_OPENCHECKSUM &quot;repository:repomd:openchecksum&quot;</code></p>
<dl>
<dt>
<dd> The checksum over the uncompressed contents of the resource.</dl>
<p> <code>REPOSITORY_REPOMD_SIZE &quot;repository:repomd:size&quot;</code></p>
<dl>
<dt>
<dd> The size of the resource file.</dl>
<h2>DELTA PACKAGE ATTRIBUTES</h2>
<p> <code>DELTA_PACKAGE_NAME &quot;delta:pkgname&quot;</code></p>
<dl>
<dt>
<dd> The target package name for the delta package. Applying the delta will recreate the target package.</dl>
<p> <code>DELTA_PACKAGE_EVR &quot;delta:pkgevr&quot;</code></p>
<dl>
<dt>
<dd> The version of the target package.</dl>
<p> <code>DELTA_PACKAGE_ARCH &quot;delta:pkgarch&quot;</code></p>
<dl>
<dt>
<dd> The architecture of the target package.</dl>
<p> <code>DELTA_LOCATION_DIR &quot;delta:locdir&quot;</code></p>
<dl>
<dt>
<dd> The directory in the repository that contains the delta package.</dl>
<p> <code>DELTA_LOCATION_NAME &quot;delta:locname&quot;</code></p>
<dl>
<dt>
<dd> The first part of the file name of the delta package.</dl>
<p> <code>DELTA_LOCATION_EVR &quot;delta:locevr&quot;</code></p>
<dl>
<dt>
<dd> The version part of the file name of the delta package.</dl>
<p> <code>DELTA_LOCATION_SUFFIX &quot;delta:locsuffix&quot;</code></p>
<dl>
<dt>
<dd> The suffix part of the file name of the delta package.</dl>
<p> <code>DELTA_LOCATION_BASE &quot;delta:locbase&quot;</code></p>
<dl>
<dt>
<dd> This attribute can be used to overwrite the repositories base url for the delta.</dl>
<p> <code>DELTA_DOWNLOADSIZE &quot;delta:downloadsize&quot;</code></p>
<dl>
<dt>
<dd> The size of the delta rpm file.</dl>
<p> <code>DELTA_CHECKSUM &quot;delta:checksum&quot;</code></p>
<dl>
<dt>
<dd> The checksum of the delta rpm file.</dl>
<p> <code>DELTA_BASE_EVR &quot;delta:baseevr&quot;</code></p>
<dl>
<dt>
<dd> The version of the package the delta was built against.</dl>
<p> <code>DELTA_SEQ_NAME &quot;delta:seqname&quot;</code></p>
<dl>
<dt>
<dd> The first part of the delta sequence, the base package name.</dl>
<p> <code>DELTA_SEQ_EVR &quot;delta:seqevr&quot;</code></p>
<dl>
<dt>
<dd> The evr part of the delta sequence, the base package evr. Identical to the DELTA_BASE_EVR attribute.</dl>
<p> <code>DELTA_SEQ_NUM &quot;delta:seqnum&quot;</code></p>
<dl>
<dt>
<dd> The last part of the delta sequence, the content selection string.</dl>
<h2>AUTHOR</h2>
<p> Michael Schroeder &lt;mls [at] suse.de&gt; </p>
<h2>Index</h2>
