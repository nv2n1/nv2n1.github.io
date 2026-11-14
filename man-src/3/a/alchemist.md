---
title: "alchemist(3)"
name: "alchemist"
section: "3"
letter: "a"
url: "/docs/linux/man/3-alchemist/"
description: "alchemist.h –"
---

<h2 class="name">NAME</h2>
<p> alchemist.h &#8211; </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/sys/types.h">sys/types.h</a>&gt; </p>
<h3>Classes</h3>
<p> struct <code>adm_bb_cap_t</code> </p>
<h3>Defines</h3>
<p> #define <code>ALCHEMIST_ABI_MAJOR_VER</code> 0 </p>
<p> #define <code>ALCHEMIST_ABI_MINOR_VER</code> 0 </p>
<p> #define <code>ADM_EDEADNODE</code> 1 </p>
<p> #define <code>ADM_EBADTYPE</code> 2 </p>
<p> #define <code>ADM_EBADNAME</code> 3 </p>
<p> #define <code>ADM_EBADDATA</code> 4 </p>
<p> #define <code>ADM_ECONSTRAINT</code> 5 </p>
<p> #define <code>ADM_ENOINDEX</code> 51 </p>
<p> #define <code>ADM_ENONAME</code> 52 </p>
<p> #define <code>ADM_ENOPATH</code> 53 </p>
<p> #define <code>ADM_EACCESSFAILED</code> 101 </p>
<p> #define <code>ADM_ENONAMESPACE</code> 102 </p>
<p> #define <code>ADM_ENOSUBSPACE</code> 103 </p>
<p> #define <code>ADM_ENOWRITE</code> 201 </p>
<p> #define <code>ADM_ENOREAD</code> 202 </p>
<p> #define <code>ADM_ENOLISTSERIAL</code> 203 </p>
<p> #define <code>ADM_ENOREADSERIAL</code> 204 </p>
<p> #define <code>ADM_ENOCACHE</code> 205 </p>
<p> #define <code>ADM_ENOBOXTYPE</code> 251 </p>
<p> #define <code>ADM_EPARSE</code> 301 </p>
<p> #define <code>AdmRefStr_str</code>(REFSTR) </p>
<p> #define <code>AdmContext_getIdentityRoot_b</code>(CONTEXT, ERROR) </p>
<p> #define <code>AdmIdentity_getParentA_b</code>(ID, ERROR) </p>
<p> #define <code>AdmIdentity_getParentB_b</code>(ID, ERROR) </p>
<p> #define <code>AdmIdentity_getContext_b</code>(ID, ERROR) </p>
<p> #define <code>AdmContext_getDataRoot_b</code>(CONTEXT, ERROR) </p>
<p> #define <code>AdmData_getContainer_b</code>(DATA, ERROR) </p>
<p> #define <code>AdmData_getPrev_b</code>(DATA, WRAP, ERROR) </p>
<p> #define <code>AdmData_getNext_b</code>(DATA, WRAP, ERROR) </p>
<p> #define <code>AdmData_getContext_b</code>(DATA, ERROR) </p>
<p> #define <code>AdmContext_getDataByPath_b</code>(CONTEXT, PATH, ERROR) </p>
<p> #define <code>AdmList_getDataByIndex_b</code>(LIST, INDEX, ERROR) </p>
<p> #define <code>AdmList_getDataByName_b</code>(LIST, NAME, ERROR) </p>
<p> #define <code>AdmList_getDataByPath_b</code>(LIST, PATH, ERROR) </p>
<p> #define <code>AdmList_addData_b</code>(LIST, TYPE, NAME, ERROR) </p>
<p> #define <code>AdmList_copyData_b</code>(LIST, DATA, ERROR) </p>
<p> #define <code>AdmList_renameCopyData_b</code>(LIST, DATA, NAME, ERROR) </p>
<p> #define <code>ADM_BBCAP_SUP_WRITE</code>(CAP) ((CAP).array[0] &amp; (1 &lt;&lt; 0)) </p>
<p> #define <code>ADM_BBCAP_SUP_READ</code>(CAP) ((CAP).array[0] &amp; (1 &lt;&lt; 1)) </p>
<p> #define <code>ADM_BBCAP_SUP_LISTSERIAL</code>(CAP) ((CAP).array[0] &amp; (1 &lt;&lt; 2)) </p>
<p> #define <code>ADM_BBCAP_SUP_READSERIAL</code>(CAP) ((CAP).array[0] &amp; (1 &lt;&lt; 3)) </p>
<p> #define <code>ADM_BBCAP_CACHED</code>(CAP) ((CAP).array[0] &amp; (1 &lt;&lt; 4)) </p>
<p> #define <code>AdmSwitchboard_getNspCfg_b</code>(CTX, NAMESPACE, ERROR) </p>
<p> #define <code>AdmSwitchboard_getSubspCfg_b</code>(CTX, SUBSPACE, ERROR) </p>
<h3>Typedefs</h3>
<p> typedef struct <code>AdmError</code> <code>AdmError</code> </p>
<p> typedef struct <code>AdmRefStr</code> <code>AdmRefStr</code> </p>
<p> typedef struct <code>AdmData</code> <code>AdmData</code> </p>
<p> typedef struct <code>AdmList</code> <code>AdmList</code> </p>
<p> typedef struct <code>AdmInt</code> <code>AdmInt</code> </p>
<p> typedef struct <code>AdmBool</code> <code>AdmBool</code> </p>
<p> typedef struct <code>AdmFloat</code> <code>AdmFloat</code> </p>
<p> typedef struct <code>AdmString</code> <code>AdmString</code> </p>
<p> typedef struct <code>AdmString</code> <code>AdmBase64</code> </p>
<p> typedef struct <code>AdmString</code> <code>AdmCopy</code> </p>
<p> typedef struct <code>AdmIdentity</code> <code>AdmIdentity</code> </p>
<p> typedef struct <code>AdmContext</code> <code>AdmContext</code> </p>
<p> typedef struct <code>AdmBlackBox</code> <code>AdmBlackBox</code> </p>
<h3>Enumerations</h3>
<p> enum <code>AdmDataType</code> { <code>ADM_TYPE_UNKNOWN</code> = 0, <code>ADM_TYPE_LIST</code> = 1, <code>ADM_TYPE_COPY</code> = 2, <code>ADM_TYPE_INT</code> = 3, <code>ADM_TYPE_FLOAT</code> = 4, <code>ADM_TYPE_BOOL</code> = 5, <code>ADM_TYPE_STRING</code> = 6, <code>ADM_TYPE_BASE64</code> = 7 } </p>
<h3>Functions</h3>
<p> void <code>AdmError_create</code> (<code>AdmError</code> **error, int num, const char *format,&#8230;)<br />
 <i>Allocate new AdmError structure. </i><br />
 void <code>AdmError_ref</code> (<code>AdmError</code> *error)<br />
 <i>Increment the ref count of an AdmError structure. </i><br />
 void <code>AdmError_unref</code> (<code>AdmError</code> *error)<br />
 <i>Decrement the ref count of an AdmError structure. </i><br />
 const char * <code>AdmError_strerr</code> (<code>AdmError</code> *error)<br />
 <i>String description of error. </i><br />
 int <code>AdmError_errno</code> (<code>AdmError</code> *error)<br />
 <i>Integer error code of error. </i><br />
 <code>AdmRefStr</code> * <code>AdmRefStr_ref</code> (<code>AdmRefStr</code> *refstr) </p>
<p> void <code>AdmRefStr_unref</code> (<code>AdmRefStr</code> *refstr) </p>
<p> size_t <code>AdmRefStr_len</code> (<code>AdmRefStr</code> *refstr) </p>
<p> <code>AdmRefStr</code> * <code>AdmRefStr_get</code> (const char *str, int force)<br />
 <i>Get an AdmRefStr. </i><br />
 <code>AdmRefStr</code> * <code>AdmRefStr_nget</code> (const char *str, size_t len, int force)<br />
 <i>Get an AdmRefStr, by length. </i><br />
 <code>AdmContext</code> * <code>AdmContext_new</code> (const char *name, unsigned int serial, <code>AdmError</code> **error)<br />
 <i>AdmContext constructor. </i><br />
 <code>AdmContext</code> * <code>AdmContext_ref</code> (<code>AdmContext</code> *context, <code>AdmError</code> **error)<br />
 <i>AdmContext reference increment. </i><br />
 void <code>AdmContext_unref</code> (<code>AdmContext</code> *context, <code>AdmError</code> **error)<br />
 <i>AdmContext reference decrement. </i><br />
 <code>AdmContext</code> * <code>AdmContext_copy</code> (<code>AdmContext</code> *context, <code>AdmError</code> **error)<br />
 <i>AdmContext copy operator. </i><br />
 <code>AdmContext</code> * <code>AdmContext_merge</code> (const char *name, unsigned int serial, <code>AdmContext</code> *contextA, <code>AdmContext</code> *contextB, <code>AdmError</code> **error)<br />
 <i>AdmContext merge operator. </i><br />
 void <code>AdmContext_flatten</code> (<code>AdmContext</code> *context, <code>AdmError</code> **error)<br />
 <i>AdmContext flatten operator. </i><br />
 void <code>AdmContext_strip</code> (<code>AdmContext</code> *context, <code>AdmError</code> **error)<br />
 <i>AdmContext strip function. </i><br />
 char * <code>AdmContext_toXML</code> (<code>AdmContext</code> *context, <code>AdmError</code> **error) </p>
<p> <code>AdmContext</code> * <code>AdmContext_fromXML</code> (const char *xml, <code>AdmError</code> **error) </p>
<p> int <code>AdmContext_readFromFile</code> (<code>AdmContext</code> **context, const char *path, <code>AdmError</code> **error) </p>
<p> int <code>AdmContext_writeToFile</code> (<code>AdmContext</code> *context, const char *path, int mode, uid_t uid, gid_t gid, <code>AdmError</code> **error) </p>
<p> <code>AdmRefStr</code> * <code>AdmContext_getMask</code> (<code>AdmContext</code> *context, unsigned int index, <code>AdmError</code> **error)<br />
 <i>AdmContext mask set accessor. </i><br />
 int <code>AdmContext_setMask</code> (<code>AdmContext</code> *context, const char *path, <code>AdmError</code> **error)<br />
 <i>AdmContext mask set mutator. </i><br />
 int <code>AdmContext_clearMaskByIndex</code> (<code>AdmContext</code> *context, unsigned int index, <code>AdmError</code> **error)<br />
 <i>AdmContext mask set element index remove. </i><br />
 int <code>AdmContext_clearMaskByPath</code> (<code>AdmContext</code> *context, const char *path, <code>AdmError</code> **error)<br />
 <i>AdmContext mask set element data path remove. </i><br />
 unsigned int <code>AdmContext_getNumMasks</code> (<code>AdmContext</code> *context, <code>AdmError</code> **error)<br />
 <i>AdmContext mask set length aggregator. </i><br />
 <code>AdmIdentity</code> * <code>AdmContext_getIdentityRoot</code> (<code>AdmContext</code> *context, <code>AdmError</code> **error)<br />
 <i>AdmContext identity root accessor. </i><br />
 <code>AdmIdentity</code> * <code>AdmIdentity_getParentA</code> (<code>AdmIdentity</code> *identity, <code>AdmError</code> **error)<br />
 <i>AdmIdentity parentA accessor. </i><br />
 <code>AdmIdentity</code> * <code>AdmIdentity_getParentB</code> (<code>AdmIdentity</code> *identity, <code>AdmError</code> **error)<br />
 <i>AdmIdentity parentB accessor. </i><br />
 <code>AdmRefStr</code> * <code>AdmIdentity_getName</code> (<code>AdmIdentity</code> *identity, <code>AdmError</code> **error)<br />
 <i>AdmIdentity name accessor. </i><br />
 int <code>AdmIdentity_setName</code> (<code>AdmIdentity</code> *identity, const char *name, <code>AdmError</code> **error)<br />
 <i>AdmIdentity name mutator. </i><br />
 unsigned int <code>AdmIdentity_getSerial</code> (<code>AdmIdentity</code> *identity, <code>AdmError</code> **error)<br />
 <i>AdmIdentity serial number accessor. </i><br />
 int <code>AdmIdentity_setSerial</code> (<code>AdmIdentity</code> *identity, unsigned int serial, <code>AdmError</code> **error)<br />
 <i>AdmIdentity serial number mutator. </i><br />
 <code>AdmIdentity</code> * <code>AdmIdentity_ref</code> (<code>AdmIdentity</code> *identity, <code>AdmError</code> **error)<br />
 <i>AdmIdentity reference increment. </i><br />
 void <code>AdmIdentity_unref</code> (<code>AdmIdentity</code> *identity, <code>AdmError</code> **error)<br />
 <i>AdmIdentity reference decrement. </i><br />
 <code>AdmContext</code> * <code>AdmIdentity_getContext</code> (<code>AdmIdentity</code> *identity, <code>AdmError</code> **error)<br />
 <i>AdmIdentity context accessor. </i><br />
 int <code>AdmIdentity_isAlive</code> (<code>AdmIdentity</code> *identity, <code>AdmError</code> **error)<br />
 <i>AdmIdentity reference check. </i><br />
 <code>AdmData</code> * <code>AdmContext_getDataRoot</code> (<code>AdmContext</code> *context, <code>AdmError</code> **error)<br />
 <i>AdmContext data root accessor. </i><br />
 <code>AdmData</code> * <code>AdmData_getContainer</code> (<code>AdmData</code> *data, <code>AdmError</code> **error)<br />
 <i>AdmData container accessor. </i><br />
 <code>AdmData</code> * <code>AdmData_getPrev</code> (<code>AdmData</code> *data, int wrap, <code>AdmError</code> **error)<br />
 <i>get the previous sibling of an AdmData element </i><br />
 <code>AdmData</code> * <code>AdmData_getNext</code> (<code>AdmData</code> *data, int wrap, <code>AdmError</code> **error)<br />
 <i>get the next sibling of an AdmData element </i><br />
 <code>AdmContext</code> * <code>AdmData_getContext</code> (<code>AdmData</code> *data, <code>AdmError</code> **error)<br />
 <i>AdmData context accessor. </i><br />
 <code>AdmData</code> * <code>AdmContext_getDataByPath</code> (<code>AdmContext</code> *context, const char *path, <code>AdmError</code> **error)<br />
 <i>AdmData path lookup. </i><br />
 <code>AdmDataType</code> <code>AdmData_getType</code> (<code>AdmData</code> *data, <code>AdmError</code> **error)<br />
 <i>AdmData type accessor. </i><br />
 <code>AdmData</code> * <code>AdmData_ref</code> (<code>AdmData</code> *data, <code>AdmError</code> **error)<br />
 <i>AdmData reference increment. </i><br />
 void <code>AdmData_unref</code> (<code>AdmData</code> *data, <code>AdmError</code> **error)<br />
 <i>AdmData reference decrement. </i><br />
 int <code>AdmData_isAlive</code> (<code>AdmData</code> *data, <code>AdmError</code> **error)<br />
 <i>AdmData reference check. </i><br />
 int <code>AdmData_unlink</code> (<code>AdmData</code> *data, <code>AdmError</code> **error)<br />
 <i>AdmData unlink operator. </i><br />
 int <code>AdmData_validName</code> (const char *name)<br />
 <i>Checks a string for name validity. </i><br />
 <code>AdmRefStr</code> * <code>AdmData_getName</code> (<code>AdmData</code> *data, <code>AdmError</code> **error)<br />
 <i>AdmData name accessor. </i><br />
 int <code>AdmData_setName</code> (<code>AdmData</code> *data, const char *name, <code>AdmError</code> **error)<br />
 <i>AdmData name mutator. </i><br />
 <code>AdmRefStr</code> * <code>AdmData_getSource</code> (<code>AdmData</code> *data, <code>AdmError</code> **error)<br />
 <i>AdmData source accessor. </i><br />
 int <code>AdmData_setSource</code> (<code>AdmData</code> *data, const char *source, <code>AdmError</code> **error)<br />
 <i>AdmData source mutator. </i><br />
 int <code>AdmData_isProtected</code> (<code>AdmData</code> *data, <code>AdmError</code> **error)<br />
 <i>AdmData protected verification. </i><br />
 int <code>AdmData_setProtected</code> (<code>AdmData</code> *data, int state, <code>AdmError</code> **error)<br />
 <i>AdmData protected mutator. </i><br />
 int <code>AdmList_isAnonymous</code> (<code>AdmList</code> *list, <code>AdmError</code> **error)<br />
 <i>AdmList anonymous verification. </i><br />
 int <code>AdmList_setAnonymous</code> (<code>AdmList</code> *list, int state, <code>AdmError</code> **error)<br />
 <i>AdmList anonymous mutator. </i><br />
 int <code>AdmList_isAtomic</code> (<code>AdmList</code> *list, <code>AdmError</code> **error)<br />
 <i>AdmList atomic verification. </i><br />
 int <code>AdmList_setAtomic</code> (<code>AdmList</code> *list, int state, <code>AdmError</code> **error)<br />
 <i>AdmList atomic mutator. </i><br />
 int <code>AdmList_isPrepend</code> (<code>AdmList</code> *list, <code>AdmError</code> **error)<br />
 <i>AdmList prepend verification. </i><br />
 int <code>AdmList_setPrepend</code> (<code>AdmList</code> *list, int state, <code>AdmError</code> **error)<br />
 <i>AdmList prepend mutator. </i><br />
 unsigned int <code>AdmList_getNumData</code> (<code>AdmList</code> *list, <code>AdmError</code> **error)<br />
 <i>AdmList length aggregator. </i><br />
 <code>AdmData</code> * <code>AdmList_getDataByIndex</code> (<code>AdmList</code> *list, unsigned int index, <code>AdmError</code> **error)<br />
 <i>AdmList child index accessor. </i><br />
 <code>AdmData</code> * <code>AdmList_getDataByName</code> (<code>AdmList</code> *list, const char *name, <code>AdmError</code> **error)<br />
 <i>AdmList child name accessor. </i><br />
 <code>AdmData</code> * <code>AdmList_getDataByPath</code> (<code>AdmList</code> *list, const char *path, <code>AdmError</code> **error)<br />
 <i>AdmList child data path accessor. </i><br />
 <code>AdmData</code> * <code>AdmList_addData</code> (<code>AdmList</code> *list, <code>AdmDataType</code> type, const char *name, <code>AdmError</code> **error)<br />
 <i>AdmList add child operator. </i><br />
 int <code>AdmList_moveData</code> (<code>AdmList</code> *list, <code>AdmData</code> *data, unsigned int index, <code>AdmError</code> **error)<br />
 <i>AdmList child move operator. </i><br />
 <code>AdmData</code> * <code>AdmList_copyData</code> (<code>AdmList</code> *list, <code>AdmData</code> *data, <code>AdmError</code> **error)<br />
 <i>AdmList copy data operator. </i><br />
 <code>AdmData</code> * <code>AdmList_renameCopyData</code> (<code>AdmList</code> *list, <code>AdmData</code> *data, const char *name, <code>AdmError</code> **error)<br />
 <i>AdmList copy data operator. </i><br />
 unsigned int <code>AdmData_getPos</code> (<code>AdmData</code> *data, <code>AdmError</code> **error)<br />
 <i>AdmList child position operator. </i><br />
 int <code>AdmInt_getValue</code> (<code>AdmInt</code> *int_scalar, <code>AdmError</code> **error)<br />
 <i>get an AdmInt&#8217;s value </i><br />
 int <code>AdmInt_setValue</code> (<code>AdmInt</code> *int_scalar, int value, <code>AdmError</code> **error)<br />
 <i>set an AdmInt&#8217;s value </i><br />
 double <code>AdmFloat_getValue</code> (<code>AdmFloat</code> *float_scalar, <code>AdmError</code> **error)<br />
 <i>get an AdmFloat&#8217;s value </i><br />
 int <code>AdmFloat_setValue</code> (<code>AdmFloat</code> *float_scalar, double value, <code>AdmError</code> **error)<br />
 <i>set an AdmFloat&#8217;s value </i><br />
 int <code>AdmBool_getValue</code> (<code>AdmBool</code> *bool_scalar, <code>AdmError</code> **error)<br />
 <i>get an AdmBool&#8217;s value </i><br />
 int <code>AdmBool_setValue</code> (<code>AdmBool</code> *bool_scalar, int value, <code>AdmError</code> **error)<br />
 <i>set an AdmBool&#8217;s value </i><br />
 <code>AdmRefStr</code> * <code>AdmString_getValue</code> (<code>AdmString</code> *string_scalar, <code>AdmError</code> **error)<br />
 <i>get an AdmString&#8217;s value </i><br />
 int <code>AdmString_setValue</code> (<code>AdmString</code> *string_scalar, const char *value, <code>AdmError</code> **error) </p>
<p> <code>AdmRefStr</code> * <code>AdmBase64_getValue</code> (<code>AdmBase64</code> *base64_scalar, <code>AdmError</code> **error) </p>
<p> int <code>AdmBase64_setValue</code> (<code>AdmBase64</code> *base64_scalar, const char *value, <code>AdmError</code> **error)<br />
 <i>Set the value of an AdmBase64 element. </i><br />
 size_t <code>AdmBase64_getBinValue</code> (<code>AdmBase64</code> *base64_scalar, void **value, <code>AdmError</code> **error)<br />
 <i>Get the binary value of an AdmBase64 element. </i><br />
 int <code>AdmBase64_setBinValue</code> (<code>AdmBase64</code> *base64_scalar, const void *value, size_t size, <code>AdmError</code> **error)<br />
 <i>Set the value of an AdmBase64 element. </i><br />
 <code>AdmRefStr</code> * <code>AdmCopy_getValue</code> (<code>AdmCopy</code> *copy_scalar, <code>AdmError</code> **error)<br />
 <i>Get the value of an AdmCopy element. </i><br />
 int <code>AdmCopy_setValue</code> (<code>AdmCopy</code> *copy_scalar, const char *value, <code>AdmError</code> **error)<br />
 <i>Set the value of an AdmCopy element. </i><br />
 <code>AdmRefStr</code> * <code>AdmBlackBox_getCacheDir</code> (<code>AdmError</code> **error) </p>
<p> int <code>AdmBlackBox_setCacheDir</code> (const char *path, <code>AdmError</code> **error) </p>
<p> <code>AdmBlackBox</code> * <code>AdmBlackBox_getBox</code> (<code>AdmList</code> *box_cfg, <code>AdmError</code> **error) </p>
<p> <code>adm_bb_cap_t</code> <code>AdmBlackBox_caps</code> (<code>AdmBlackBox</code> *box, <code>AdmError</code> **error)<br />
 <i>AdmBlackBox capability querry. </i><br />
 void <code>AdmBlackBox_ref</code> (<code>AdmBlackBox</code> *box, <code>AdmError</code> **error)<br />
 <i>AdmBlackbox reference increment. </i><br />
 void <code>AdmBlackBox_unref</code> (<code>AdmBlackBox</code> *box, <code>AdmError</code> **error)<br />
 <i>AdmBlackbox reference decrement. </i><br />
 <code>AdmContext</code> * <code>AdmBlackBox_read</code> (<code>AdmBlackBox</code> *box, <code>AdmError</code> **error)<br />
 <i>AdmBlackbox read operator. </i><br />
 int <code>AdmBlackBox_listSerial</code> (<code>AdmBlackBox</code> *box, unsigned int *array, unsigned int array_len, unsigned int top_serial, <code>AdmError</code> **error)<br />
 <i>AdmBlackbox serial list request. </i><br />
 <code>AdmContext</code> * <code>AdmBlackBox_readSerial</code> (<code>AdmBlackBox</code> *box, unsigned int serial, <code>AdmError</code> **error)<br />
 <i>AdmBlackbox serial list request. </i><br />
 int <code>AdmBlackBox_write</code> (<code>AdmBlackBox</code> *box, <code>AdmContext</code> *context, <code>AdmError</code> **error)<br />
 <i>AdmBlackbox write operator. </i><br />
 unsigned int <code>AdmBlackBox_getMark</code> (<code>AdmBlackBox</code> *box, const char *mark, <code>AdmError</code> **error)<br />
 <i>AdmBlackBox mark accessor. </i><br />
 int <code>AdmBlackBox_setMark</code> (<code>AdmBlackBox</code> *box, const char *mark, <code>AdmError</code> **error)<br />
 <i>AdmBlackBox mark mutator. </i><br />
 int <code>AdmBlackBox_clearMark</code> (<code>AdmBlackBox</code> *box, const char *mark, <code>AdmError</code> **error)<br />
 <i>AdmBlackbox mark destructor. </i><br />
 <code>AdmRefStr</code> * <code>AdmSwitchboard_getSwbDir</code> (<code>AdmError</code> **error) </p>
<p> int <code>AdmSwitchboard_setSwbDir</code> (const char *path, <code>AdmError</code> **error) </p>
<p> int <code>AdmSwitchboard_markNsp</code> (const char *namespace, const char *subspace, const char *mark, <code>AdmError</code> **error) </p>
<p> int <code>AdmSwitchboard_markNspWithConfig</code> (<code>AdmList</code> *namespace_cfg, const char *subspace, const char *mark, <code>AdmError</code> **error) </p>
<p> int <code>AdmSwitchboard_checkNspMark</code> (const char *namespace, const char *subspace, const char *mark, <code>AdmError</code> **error) </p>
<p> int <code>AdmSwitchboard_checkNspMarkWithConfig</code> (<code>AdmList</code> *namespace_cfg, const char *subspace, const char *mark, <code>AdmError</code> **error) </p>
<p> <code>AdmContext</code> * <code>AdmSwitchboard_readNsp</code> (const char *namespace, const char *subspace, unsigned int depth, <code>AdmError</code> **error) </p>
<p> <code>AdmContext</code> * <code>AdmSwitchboard_readNspWithConfig</code> (<code>AdmList</code> *namespace_cfg, const char *subspace, unsigned int depth, <code>AdmError</code> **error) </p>
<p> int <code>AdmSwitchboard_writeNsp</code> (const char *namespace, const char *subspace, <code>AdmContext</code> *context, <code>AdmError</code> **error) </p>
<p> int <code>AdmSwitchboard_writeNspWithConfig</code> (<code>AdmList</code> *namespace_cfg, const char *subspace, <code>AdmContext</code> *context, <code>AdmError</code> **error) </p>
<p> <code>AdmContext</code> * <code>AdmSwitchboard_readNspCtx</code> (const char *namespace, <code>AdmError</code> **error)<br />
 <i>read a switchboard namespace configuration from the system </i><br />
 int <code>AdmSwitchboard_writeNspCtx</code> (const char *namespace, <code>AdmContext</code> *namespace_ctx, int mode, uid_t uid, gid_t gid, <code>AdmError</code> **error)<br />
 <i>writes a switchboard namespace configuration to the system </i><br />
 <code>AdmList</code> * <code>AdmSwitchboard_getNspCfg</code> (<code>AdmContext</code> *namespace_ctx, const char *namespace, <code>AdmError</code> **error) </p>
<p> <code>AdmList</code> * <code>AdmSwitchboard_getSubspCfg</code> (<code>AdmList</code> *namespace_cfg, const char *subspace, <code>AdmError</code> **error) </p>
<p> <code>AdmBlackBox</code> * <code>AdmSwitchboard_getBox</code> (<code>AdmList</code> *subspace_cfg, const char *box_name, <code>AdmError</code> **error) </p>
<h2>Define Documentation</h2>
<h3>#define ALCHEMIST_ABI_MAJOR_VER 0</h3>
<h3>#define ALCHEMIST_ABI_MINOR_VER 0</h3>
<h3>#define ADM_EDEADNODE 1</h3>
<h3>#define ADM_EBADTYPE 2</h3>
<h3>#define ADM_EBADNAME 3</h3>
<h3>#define ADM_EBADDATA 4</h3>
<h3>#define ADM_ECONSTRAINT 5</h3>
<h3>#define ADM_ENOINDEX 51</h3>
<h3>#define ADM_ENONAME 52</h3>
<h3>#define ADM_ENOPATH 53</h3>
<h3>#define ADM_EACCESSFAILED 101</h3>
<h3>#define ADM_ENONAMESPACE 102</h3>
<h3>#define ADM_ENOSUBSPACE 103</h3>
<h3>#define ADM_ENOWRITE 201</h3>
<h3>#define ADM_ENOREAD 202</h3>
<h3>#define ADM_ENOLISTSERIAL 203</h3>
<h3>#define ADM_ENOREADSERIAL 204</h3>
<h3>#define ADM_ENOCACHE 205</h3>
<h3>#define ADM_ENOBOXTYPE 251</h3>
<h3>#define ADM_EPARSE 301</h3>
<h3>#define AdmRefStr_str(REFSTR)</h3>
<p> <code>Value:</code> </p>
<pre><code>
({         AdmRefStr *__tok = (REFSTR);         (const char *) __tok; })
</code></pre>
<h3>#define AdmContext_getIdentityRoot_b(CONTEXT, ERROR)</h3>
<p> <code>Value:</code> </p>
<p>({         AdmError **__err = (ERROR);         AdmIdentity *__id;         __id = AdmContext_getIdentityRoot((CONTEXT), __err);         if (__id != NULL)                 AdmIdentity_unref(__id, __err);         __id; })</p>
<h3>#define AdmIdentity_getParentA_b(ID, ERROR)</h3>
<p> <code>Value:</code> </p>
<p>({         AdmError **__err = (ERROR);         AdmIdentity *__id;         __id = AdmIdentity_getParentA((ID), __err);         if (__id != NULL)                 AdmIdentity_unref(__id, __err);         __id; })</p>
<h3>#define AdmIdentity_getParentB_b(ID, ERROR)</h3>
<p> <code>Value:</code> </p>
<p>({         AdmError **__err = (ERROR);         AdmIdentity *__id;         __id = AdmIdentity_getParentB((ID), __err);         if (__id != NULL)                 AdmIdentity_unref(__id, __err);         __id; })</p>
<h3>#define AdmIdentity_getContext_b(ID, ERROR)</h3>
<p> <code>Value:</code> </p>
<p>({         AdmError **__err = (ERROR);         AdmContext *__ctx;         __ctx = AdmIdentity_getContext((ID), __err);         if (__ctx != NULL)                 AdmContext_unref(__ctx, __err);         __ctx; })</p>
<h3>#define AdmContext_getDataRoot_b(CONTEXT, ERROR)</h3>
<p> <code>Value:</code> </p>
<p>({         AdmError **__err = (ERROR);         AdmData *__data;         __data = AdmContext_getDataRoot((CONTEXT), __err);         if (__data != NULL)                 AdmData_unref(__data, __err);         __data; })</p>
<h3>#define AdmData_getContainer_b(DATA, ERROR)</h3>
<p> <code>Value:</code> </p>
<p>({         AdmError **__err = (ERROR);         AdmData *__data;         __data = AdmData_getContainer((DATA), __err);         if (__data != NULL)                 AdmData_unref(__data, __err);         __data; })</p>
<h3>#define AdmData_getPrev_b(DATA, WRAP, ERROR)</h3>
<p> <code>Value:</code> </p>
<p>({         AdmError **__err = (ERROR);         AdmData *__data;         __data = AdmData_getPrev((DATA), (WRAP), __err);         if (__data != NULL)                 AdmData_unref(__data, __err);         __data; })</p>
<h3>#define AdmData_getNext_b(DATA, WRAP, ERROR)</h3>
<p> <code>Value:</code> </p>
<p>({         AdmError **__err = (ERROR);         AdmData *__data;         __data = AdmData_getNext((DATA), (WRAP), __err);         if (__data != NULL)                 AdmData_unref(__data, __err);         __data; })</p>
<h3>#define AdmData_getContext_b(DATA, ERROR)</h3>
<p> <code>Value:</code> </p>
<p>({         AdmError **__err = (ERROR);         AdmContext *__ctx;         __ctx = AdmData_getContext((DATA), __err);         if (__ctx != NULL)                 AdmContext_unref(__ctx, __err);         __ctx; })</p>
<h3>#define AdmContext_getDataByPath_b(CONTEXT, PATH, ERROR)</h3>
<p> <code>Value:</code> </p>
<p>({         AdmError **__err = (ERROR);         AdmData *__data;         __data = AdmContext_getDataByPath((CONTEXT), (PATH), __err);         if (__data != NULL)                 AdmData_unref(__data, __err);         __data; })</p>
<h3>#define AdmList_getDataByIndex_b(LIST, INDEX, ERROR)</h3>
<p> <code>Value:</code> </p>
<p>({         AdmError **__err = (ERROR);         AdmData *__data;         __data = AdmList_getDataByIndex((LIST), (INDEX), __err);         if (__data != NULL)                 AdmData_unref(__data, __err);         __data; })</p>
<h3>#define AdmList_getDataByName_b(LIST, NAME, ERROR)</h3>
<p> <code>Value:</code> </p>
<p>({         AdmError **__err = (ERROR);         AdmData *__data;         __data = AdmList_getDataByName((LIST), (NAME), __err);         if (__data != NULL)                 AdmData_unref(__data, __err);         __data; })</p>
<h3>#define AdmList_getDataByPath_b(LIST, PATH, ERROR)</h3>
<p> <code>Value:</code> </p>
<p>({         AdmError **__err = (ERROR);         AdmData *__data;         __data = AdmList_getDataByPath((LIST), (PATH), __err);         if (__data != NULL)                 AdmData_unref(__data, __err);         __data; })</p>
<h3>#define AdmList_addData_b(LIST, TYPE, NAME, ERROR)</h3>
<p> <code>Value:</code> </p>
<p>({         AdmError **__err = (ERROR);         AdmData *__data;         __data = AdmList_addData((LIST), (TYPE), (NAME), __err);         if (__data != NULL)                 AdmData_unref(__data, __err);         __data; })</p>
<h3>#define AdmList_copyData_b(LIST, DATA, ERROR)</h3>
<p> <code>Value:</code> </p>
<p>({         AdmError **__err = (ERROR);         AdmData *__data;         __data = AdmList_copyData((LIST), (DATA), __err);         if (__data != NULL)                 AdmData_unref(__data, __err);         __data; })</p>
<h3>#define AdmList_renameCopyData_b(LIST, DATA, NAME, ERROR)</h3>
<p> <code>Value:</code> </p>
<p>({         AdmError **__err = (ERROR);         AdmData *__data;         __data = AdmList_renameCopyData((LIST), (DATA), (NAME), __err);         if (__data != NULL)                 AdmData_unref(__data, __err);         __data; })</p>
<h3>#define ADM_BBCAP_SUP_WRITE(CAP) ((CAP).array[0] &amp; (1 &lt;&lt; 0))</h3>
<h3>#define ADM_BBCAP_SUP_READ(CAP) ((CAP).array[0] &amp; (1 &lt;&lt; 1))</h3>
<h3>#define ADM_BBCAP_SUP_LISTSERIAL(CAP) ((CAP).array[0] &amp; (1 &lt;&lt; 2))</h3>
<h3>#define ADM_BBCAP_SUP_READSERIAL(CAP) ((CAP).array[0] &amp; (1 &lt;&lt; 3))</h3>
<h3>#define ADM_BBCAP_CACHED(CAP) ((CAP).array[0] &amp; (1 &lt;&lt; 4))</h3>
<h3>#define AdmSwitchboard_getNspCfg_b(CTX, NAMESPACE, ERROR)</h3>
<p> <code>Value:</code> </p>
<p>({         AdmError **__err = (ERROR);         AdmList *__list;         __list = AdmSwitchboard_getNspCfg((CTX), (NAMESPACE), __err);         if (__list != NULL)                 AdmData_unref((AdmData *) __list, __err);         __list; })</p>
<h3>#define AdmSwitchboard_getSubspCfg_b(CTX, SUBSPACE, ERROR)</h3>
<p> <code>Value:</code> </p>
<p>({         AdmError **__err = (ERROR);         AdmList *__list;         __list = AdmSwitchboard_getSubspCfg((CTX), (SUBSPACE), __err);         if (__list != NULL)                 AdmData_unref((AdmData *) __list, __err);         __list; })</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>AdmError</code> <code>AdmError</code></h3>
<h3>typedef struct <code>AdmRefStr</code> <code>AdmRefStr</code></h3>
<h3>typedef struct <code>AdmData</code> <code>AdmData</code></h3>
<h3>typedef struct <code>AdmList</code> <code>AdmList</code></h3>
<h3>typedef struct <code>AdmInt</code> <code>AdmInt</code></h3>
<h3>typedef struct <code>AdmBool</code> <code>AdmBool</code></h3>
<h3>typedef struct <code>AdmFloat</code> <code>AdmFloat</code></h3>
<h3>typedef struct <code>AdmString</code> <code>AdmString</code></h3>
<h3>typedef struct <code>AdmString</code> <code>AdmBase64</code></h3>
<h3>typedef struct <code>AdmString</code> <code>AdmCopy</code></h3>
<h3>typedef struct <code>AdmIdentity</code> <code>AdmIdentity</code></h3>
<h3>typedef struct <code>AdmContext</code> <code>AdmContext</code></h3>
<h3>typedef struct <code>AdmBlackBox</code> <code>AdmBlackBox</code></h3>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>AdmDataType</code></h3>
<p> <code>Enumerator: </code></p>
<dl>
<dt><i>ADM_TYPE_UNKNOWN </i></p>
<dd>
<dt><i>ADM_TYPE_LIST </i></p>
<dd>
<dt><i>ADM_TYPE_COPY </i></p>
<dd>
<dt><i>ADM_TYPE_INT </i></p>
<dd>
<dt><i>ADM_TYPE_FLOAT </i></p>
<dd>
<dt><i>ADM_TYPE_BOOL </i></p>
<dd>
<dt><i>ADM_TYPE_STRING </i></p>
<dd>
<dt><i>ADM_TYPE_BASE64 </i></p>
<dd>
</dl>
<h2>Function Documentation</h2>
<h3>void AdmError_create (<code>AdmError</code> ** error, int num, const char * format, &#8230;)</h3>
<p> Constructor/allocator for our AdmError structure. Fails safely and silently if error is NULL. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The pointer to the AdmError pointer in which the newly allocated AdmError structure will be returned.<br />
 <i>num</i> The integer error code of the new AdmError structure.<br />
 <i>format</i> The output format in <a href="/docs/linux/man/3-printf/">printf</a>(3) format.<br />
 <i>&#8230;</i> The variable arguments for the <a href="/docs/linux/man/3-printf/">printf</a>(3) format.</dl>
<h3>void AdmError_ref (<code>AdmError</code> * error)</h3>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The pointer to the AdmError structure to be deallocated.</dl>
<h3>void AdmError_unref (<code>AdmError</code> * error)</h3>
<p> Decrements the reference count of the given AdmError function, and deallocates it when the count reaches 0. This function must only be called by reference holders. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The pointer to the AdmError structure to be deallocated.</dl>
<h3>const char* AdmError_strerr (<code>AdmError</code> * error)</h3>
<p> Returns the error string of the given AdmError structure. The error string returned is guaranteed for only as long as the AdmError is refed. Users that want a copy, should make one. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The pointer to the AdmError structure.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The character string that contains the description of the error of the given AdmError structure.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Based on the <a href="/docs/linux/man/3-strerror/">strerror</a>(3) *NIX C library.</dl>
<h3>int AdmError_errno (<code>AdmError</code> * error)</h3>
<p> Returns the error code of the given AdmError structure. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The pointer to the AdmError structure.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The int error code of the given AdmError structure. See admerror.h for a list of valid error code.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Based on <a href="/docs/linux/man/3-errno/">errno</a>(3) *NIX C library.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>AdmError</code></dl>
<h3><code>AdmRefStr</code>* AdmRefStr_ref (<code>AdmRefStr</code> * refstr)</h3>
<h3>void AdmRefStr_unref (<code>AdmRefStr</code> * refstr)</h3>
<h3>size_t AdmRefStr_len (<code>AdmRefStr</code> * refstr)</h3>
<h3><code>AdmRefStr</code>* AdmRefStr_get (const char * str, int force)</h3>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>str</i> the string to match the AdmRefStr to<br />
 <i>force</i> if we should create a matching AdmRefStr if one does not already exist</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the unique matching AdmRefStr, or NULL if there is no match</dl>
<h3><code>AdmRefStr</code>* AdmRefStr_nget (const char * str, size_t len, int force)</h3>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>str</i> the string to match the AdmRefStr to<br />
 <i>len</i> the lenght of the string, as strlen would report it<br />
 <i>force</i> if we should create a matching AdmRefStr if one does not already exist</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the unique matching AdmRefStr, or NULL if there is no match</dl>
<h3><code>AdmContext</code>* AdmContext_new (const char * name, unsigned int serial, <code>AdmError</code> ** error)</h3>
<p> AdmContext_new: create a new AdmContext element. </p>
<p> This function creates a new AdmContext element. Its root id node will be initialized using the passed name and serial. The returned AdmContext will be given a ref for the caller. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>name</i> The name of the new AdmContext.<br />
 <i>serial</i> The serial number of the new AdmContext.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The pointer to the new AdmContext element or NULL on failure.</dl>
<h3><code>AdmContext</code>* AdmContext_ref (<code>AdmContext</code> * context, <code>AdmError</code> ** error)</h3>
<p> AdmContext_ref: ref an AdmContext element. </p>
<p> Increases the refcount of an AdmContext element </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> The AdmContext to increase the reference to.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The AdmContext</dl>
<h3>void AdmContext_unref (<code>AdmContext</code> * context, <code>AdmError</code> ** error)</h3>
<p> AdmContext_unref: unref an AdmContext element. </p>
<p> Unrefs an AdmContext. This will free the context, and all its children, when the ref count reaches 0. It is an error for an entity which does not own a ref to a context to call AdmContext_unref. AdmContext refs can be acquired only by calls to AdmContext_new, AdmContext_copy, AdmContext_merge, AdmContext_fromXML, and AdmContext_ref. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> The AdmContext to decrease the reference to.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<h3><code>AdmContext</code>* AdmContext_copy (<code>AdmContext</code> * context, <code>AdmError</code> ** error)</h3>
<p> This function creates a full depth copy of an AdmContext element. It is one of the AdmContext refing functions. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> The pointer to the AdmContext element to be copied.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The pointer to the copied AdmContext element.</dl>
<h3><code>AdmContext</code>* AdmContext_merge (const char * name, unsigned int serial, <code>AdmContext</code> * contextA, <code>AdmContext</code> * contextB, <code>AdmError</code> ** error)</h3>
<p> AdmContext_merge: merge two AdmContext elements into a third. </p>
<p> This is the heart function of the Alchemist. It performs the context merge algorithm upon two contexts, and returns the result. It is also one of the refing functions, as the returned child is refed for the caller. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>name</i> The name of the new AdmContext.<br />
 <i>serial</i> The serial number of the new AdmContext.<br />
 <i>contextA</i> The pointer to the first AdmContext element.<br />
 <i>contextB</i> The pointer to the second AdmContext element.<br />
 <i>error</i> Optional pointer to an AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The pointer to the new AdmContext element which contains the result of the merge operation of contextA and contextB or NULL on failure.</dl>
<h3>void AdmContext_flatten (<code>AdmContext</code> * context, <code>AdmError</code> ** error)</h3>
<p> AdmContext_flatten: flatten an AdmContext element. </p>
<p> This function strips all masks and AdmCopy elements from an AdmContext element. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> The pointer to the AdmContext element.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<h3>void AdmContext_strip (<code>AdmContext</code> * context, <code>AdmError</code> ** error)</h3>
<p> AdmContext_strip: strip an AdmContext&#8217;s id tree. </p>
<p> This function strips all ids except for the root id from an AdmContext&#8217;s id tree. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> The pointer to the AdmContext element.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<h3>char* AdmContext_toXML (<code>AdmContext</code> * context, <code>AdmError</code> ** error)</h3>
<h3><code>AdmContext</code>* AdmContext_fromXML (const char * xml, <code>AdmError</code> ** error)</h3>
<h3>int AdmContext_readFromFile (<code>AdmContext</code> ** context, const char * path, <code>AdmError</code> ** error)</h3>
<h3>int AdmContext_writeToFile (<code>AdmContext</code> * context, const char * path, int mode, uid_t uid, gid_t gid, <code>AdmError</code> ** error)</h3>
<h3><code>AdmRefStr</code>* AdmContext_getMask (<code>AdmContext</code> * context, unsigned int index, <code>AdmError</code> ** error)</h3>
<p> AdmContext_getMask: Gets a mask element from an AdmContext by index. </p>
<p> This function is used to request the index&#8217;th mask of an AdmContext element&#8217;s mask set. The string returned must be considered const and volatile, and if it is needed for long periods of time, the programmer should copy it. </p>
<p> Specifically, it is guranteed for only so long as the AdmContext element is refed, and the mask is not cleared. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> The AdmContext to use.<br />
 <i>index</i> The index of the mask set element to get.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The mask set element AdmRefStr.</dl>
<h3>int AdmContext_setMask (<code>AdmContext</code> * context, const char * path, <code>AdmError</code> ** error)</h3>
<p> AdmContext_setMask: set a mask in an AdmContext element&#8217;s mask set. </p>
<p> This function adds a mask path to an AdmContext element&#8217;s mask set. It will quietly handle duplicate paths. Blank paths will not be added. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> The AdmContext to use.<br />
 <i>path</i> The string of the mask set element to be added.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 on error, 0 on success</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This could be made much faster, if we searched the set only once.</dl>
<h3>int AdmContext_clearMaskByIndex (<code>AdmContext</code> * context, unsigned int index, <code>AdmError</code> ** error)</h3>
<p> AdmContext_clearMaskByIndex: remove a mask entry from an AdmContext by index. </p>
<p> This function removes a mask entry from an AdmContext element by searching against the passed index. It is an error to index past the end of the mask set. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> The AdmContext to use.<br />
 <i>index</i> The index of the mask set element to remove.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 on error, 0 on success</dl>
<h3>int AdmContext_clearMaskByPath (<code>AdmContext</code> * context, const char * path, <code>AdmError</code> ** error)</h3>
<p> AdmContext_clearMaskByPath: remove a mask entry from an AdmContext by string. </p>
<p> This function removes a mask entry from an AdmContext element by searching against the passed string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> The AdmContext to use.<br />
 <i>path</i> The data path of the mask set element to remove.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 on error, 0 on success</dl>
<h3>unsigned int AdmContext_getNumMasks (<code>AdmContext</code> * context, <code>AdmError</code> ** error)</h3>
<p> AdmContext_getNumMasks: Gets the number of masks in an AdmContext&#8217;s mask set. </p>
<p> This function returns the number of masks in an AdmContext&#8217;s mask set. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> The AdmContext to use.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The number of mask set element of the given AdmContext.</dl>
<h3><code>AdmIdentity</code>* AdmContext_getIdentityRoot (<code>AdmContext</code> * context, <code>AdmError</code> ** error)</h3>
<p> AdmContext_getIdentityRoot: Get the root AdmIdentity element of an AdmContext&#8217;s id tree. </p>
<p> This function gets the root node AdmIdentity element of an AdmContext element&#8217;s id tree. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> The AdmContext of which we want to get the root AdmIdentity.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The pointer to the root AdmIdentity element.</dl>
<h3><code>AdmIdentity</code>* AdmIdentity_getParentA (<code>AdmIdentity</code> * identity, <code>AdmError</code> ** error)</h3>
<p> AdmIdentity_getParentA: Get the A parent of an AdmIdentity element. </p>
<p> This function returns the A parent of an AdmIdentity element, if it exists. Otherwise, it returns NULL. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>identity</i> The AdmIdentity of which to get the first parent.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The AdmIdentity pointer to the first parent.</dl>
<h3><code>AdmIdentity</code>* AdmIdentity_getParentB (<code>AdmIdentity</code> * identity, <code>AdmError</code> ** error)</h3>
<p> AdmIdentity_getParentB: Get the B parent of an AdmIdentity element. </p>
<p> This function returns the B parent of an AdmIdentity element, if it exists. Otherwise, it returns NULL. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>identity</i> The AdmIdentity of which to get the second parent.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The AdmIdentity pointer to the first parent.</dl>
<h3><code>AdmRefStr</code>* AdmIdentity_getName (<code>AdmIdentity</code> * identity, <code>AdmError</code> ** error)</h3>
<p> AdmIdentity_getName: Get the name of an AdmIdentity element. </p>
<p> This function is used to request the name of an AdmIdentity element. The string returned must be considered const and volatile, and if it is needed for long periods of time, the programmer should copy it. </p>
<p> Specifically, it is guranteed for only so long as the AdmCopy element is refed, and its value is not changed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>identity</i> The AdmIdentity of which to get the name.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The name of the given AdmIdentity in an AdmRefStr.</dl>
<h3>int AdmIdentity_setName (<code>AdmIdentity</code> * identity, const char * name, <code>AdmError</code> ** error)</h3>
<p> AdmIdentity_setName: Set the name of an AdmIdentity element. </p>
<p> This function sets the name of an AdmIdentity element. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>identity</i> The AdmIdentity of which to set the name.<br />
 <i>name</i> The new name of the AdmIdentity.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 on error, 0 on success</dl>
<h3>unsigned int AdmIdentity_getSerial (<code>AdmIdentity</code> * identity, <code>AdmError</code> ** error)</h3>
<p> AdmIdentity_getSerial: Get the serial number of an AdmIdentity element. </p>
<p> This function gets the serial number of an AdmIdentity element. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>identity</i> The AdmIdentity of which to get the serial number.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The serial number of the given AdmIdentity.</dl>
<h3>int AdmIdentity_setSerial (<code>AdmIdentity</code> * identity, unsigned int serial, <code>AdmError</code> ** error)</h3>
<p> AdmIdentity_setSerial: Set the serial number of an AdmIdentity element. </p>
<p> This function sets the serial number of an AdmIdentity element. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>identity</i> The AdmIdentity of which to set the serial number.<br />
 <i>name</i> The new serial number of the AdmIdentity.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 on error, 0 on success</dl>
<h3><code>AdmIdentity</code>* AdmIdentity_ref (<code>AdmIdentity</code> * identity, <code>AdmError</code> ** error)</h3>
<p> AdmIdentity_ref: ref an AdmIdentity element. </p>
<p> This function refs an AdmIdentity element. It is the only way to acquire a ref to an AdmIdentity element. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>identity</i> The AdmIdentity to increase the reference to.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The AdmIdentity (for convienience).</dl>
<h3>void AdmIdentity_unref (<code>AdmIdentity</code> * identity, <code>AdmError</code> ** error)</h3>
<p> AdmIdentity_unref: unref an AdmIdentity element. </p>
<p> This function unrefs an AdmIdentity element, and frees it if the refcount reaches 0. It must only be called by entities which own a ref to the AdmIdentity element. AdmIdentity refs can only be aquired by calling AdmIdentity_ref. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>identity</i> The AdmIdentity to decrease the reference to.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<h3><code>AdmContext</code>* AdmIdentity_getContext (<code>AdmIdentity</code> * identity, <code>AdmError</code> ** error)</h3>
<p> AdmIdentity_getContext: Get the context of an AdmIdentity element. </p>
<p> This function returns a pointer to the AdmContext in which this AdmIdentity element exists. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>id</i> The pointer to the AdmIdentity element.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The pointer to the AdmContext of the given AdmIdentity.</dl>
<h3>int AdmIdentity_isAlive (<code>AdmIdentity</code> * identity, <code>AdmError</code> ** error)</h3>
<p> AdmIdentity_isAlive: check the lifecycle status of an AdmIdentity element. </p>
<p> This function checks the lifecycle status of an AdmIdentity element. It is used to tell if an element is still linked against an AdmContext, and is &#8216;alive&#8217;; or if it is not, and is &#8216;dead&#8217;. </p>
<p> A dead element must have a reference held against it that is not its container&#8217;s reference. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>identity</i> The AdmIdentity to check.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> TRUE if Identity is still referenced, FALSE otherwise.</dl>
<h3><code>AdmData</code>* AdmContext_getDataRoot (<code>AdmContext</code> * context, <code>AdmError</code> ** error)</h3>
<p> AdmContext_getDataRoot: Get the root AdmData element of an AdmContext&#8217;s data tree. </p>
<p> This function gets the root AdmData element of an AdmContext&#8217;s data tree. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> The AdmContext of which we want to get the AdmData root.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The pointer to the root AdmData element.</dl>
<h3><code>AdmData</code>* AdmData_getContainer (<code>AdmData</code> * data, <code>AdmError</code> ** error)</h3>
<p> AdmData_getContainer: Get the container of an AdmData element. </p>
<p> This function returns a pointer to the AdmData element which contains this AdmData element. For the root node, it will return a pointer to the AdmData element it was passed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> The AdmData of which we want to get the container (parent).<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The container/parent of the given AdmData element.</dl>
<h3><code>AdmData</code>* AdmData_getPrev (<code>AdmData</code> * data, int wrap, <code>AdmError</code> ** error)</h3>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> The AdmData element<br />
 <i>wrap</i> specify if we should wrap round the begining of the list<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the previous AdmData element</dl>
<h3><code>AdmData</code>* AdmData_getNext (<code>AdmData</code> * data, int wrap, <code>AdmError</code> ** error)</h3>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> The AdmData element<br />
 <i>wrap</i> specify if we should wrap round the end of the list<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the next AdmData element</dl>
<h3><code>AdmContext</code>* AdmData_getContext (<code>AdmData</code> * data, <code>AdmError</code> ** error)</h3>
<p> AdmData_getContext: Get the context of an AdmData element. </p>
<p> This function returns a pointer to the AdmContext in which this AdmData element exists. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> The AdmData of which we want to get the context.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The context of the given AdmData element.</dl>
<h3><code>AdmData</code>* AdmContext_getDataByPath (<code>AdmContext</code> * context, const char * path, <code>AdmError</code> ** error)</h3>
<p> AdmContext_getDataByPath: Gets an AdmData element from an AdmContext by path. </p>
<p> This function does path lookups against AdmContext element&#8217;s data trees. It will give an error if no matching AdmData element is found. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> The AdmContext we want to search.<br />
 <i>path</i> The data path of the AdmData element to look up.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The pointer to the found AdmData element or NULL on failure.</dl>
<h3><code>AdmDataType</code> AdmData_getType (<code>AdmData</code> * data, <code>AdmError</code> ** error)</h3>
<p> AdmData_getType: Get the type of an AdmData element. </p>
<p> This function gets the type of an AdmData element </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> The AdmData of which we want to get the data type.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The data type of the given AdmData element.</dl>
<h3><code>AdmData</code>* AdmData_ref (<code>AdmData</code> * data, <code>AdmError</code> ** error)</h3>
<p> AdmData_ref: ref an AdmData element. </p>
<p> This function refs an AdmData element. It is the only way to aquire a ref to an AdmData element. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> The AdmData to increase the reference to.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The AdmData element</dl>
<h3>void AdmData_unref (<code>AdmData</code> * data, <code>AdmError</code> ** error)</h3>
<p> AdmData_unref: unref an AdmData element. </p>
<p> This function unrefs an AdmData element, and frees it if the refcount reaches 0. It must only be called by entities which own a ref to the AdmData element. AdmData refs can only be aquired by calling AdmData_ref. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> The AdmData to decrease the reference to.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<h3>int AdmData_isAlive (<code>AdmData</code> * data, <code>AdmError</code> ** error)</h3>
<p> AdmData_isAlive: check the lifecycle status of an AdmData element. </p>
<p> This function checks the lifecycle status of an AdmData element. It is used to tell if an element is still linked against an AdmContext, and is &#8216;alive&#8217;; or if it is not, and is &#8216;dead&#8217;. </p>
<p> A dead element must have a reference held against it that is not its container&#8217;s reference. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> The AdmData to check.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> TRUE if Data is still referenced, FALSE otherwise.</dl>
<h3>int AdmData_unlink (<code>AdmData</code> * data, <code>AdmError</code> ** error)</h3>
<p> AdmData_unlink: Unlink an AdmData element from its container. </p>
<p> This function recursively unlinks an AdmData element from its containing AdmData element. It unrefs each element which it unlinks, as they loose their parents reference. It is an error to unlink the root node, and will fail. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> The AdmData to unlink.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 on error, 0 on success</dl>
<h3>int AdmData_validName (const char * name)</h3>
<p> Checks a string to determine if it is a valid AdmData name. A valid name is of the form: Name = (Letter | &#8216;_&#8217;) (Letter | Digit | &#8216;_&#8217; | &#8216;-&#8216; | &#8216;.&#8217;){0,254} Letter = [&#8216;a&#8217; &#8211; &#8216;z&#8217;] | [&#8216;A&#8217; &#8211; &#8216;Z&#8217;] Digit = [&#8216;0&#8217; &#8211; &#8216;9&#8217;] </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>name</i> The string to check.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 1 if the name is valid, 0 if the name is not.</dl>
<h3><code>AdmRefStr</code>* AdmData_getName (<code>AdmData</code> * data, <code>AdmError</code> ** error)</h3>
<p> AdmData_getName: Get the name of an AdmData element. </p>
<p> This function is used to request the name of an AdmData element. The string returned must be considered const and volatile, and if it is needed for long periods of time, the programmer should copy it. </p>
<p> Specifically, it is guranteed for only so long as the AdmData element is refed, and its name is not changed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> The AdmData of which we want to get the name.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The name of the given AdmData element.</dl>
<h3>int AdmData_setName (<code>AdmData</code> * data, const char * name, <code>AdmError</code> ** error)</h3>
<p> AdmData_setName: Set the name of an AdmData element. </p>
<p> This function sets the name of an AdmData element to a copy of the passed string. </p>
<p> It will not alter the root node, and it is an error to attempt it. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> The AdmData of which we want to set the name.<br />
 <i>name</i> The new name of the AdmData element.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 on error, 0 on success</dl>
<h3><code>AdmRefStr</code>* AdmData_getSource (<code>AdmData</code> * data, <code>AdmError</code> ** error)</h3>
<p> AdmData_getSource: Get the source of an AdmData element. </p>
<p> This function is used to request the source of an AdmData element. The string returned must be considered const and volatile, and if it is needed for long periods of time, the programmer should copy it. </p>
<p> Specifically, it is guranteed for only so long as the AdmData element is refed, and its source is not changed. The source of the root data node changes every time the name of the root id node changes. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> The AdmData of which we want to get the source.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The source of the given AdmData element.</dl>
<h3>int AdmData_setSource (<code>AdmData</code> * data, const char * source, <code>AdmError</code> ** error)</h3>
<p> AdmData_setSource: Set the source of an AdmData element. </p>
<p> This function sets the source of an AdmData element to a copy of the passed string. </p>
<p> It will not alter the root node, and it is an error to attempt it. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> The AdmData of which we want to set the source.<br />
 <i>name</i> The new source of the AdmData element.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 on error, 0 on success</dl>
<h3>int AdmData_isProtected (<code>AdmData</code> * data, <code>AdmError</code> ** error)</h3>
<p> AdmData_isProtected: Get the state of an AdmData&#8217;s protected flag. </p>
<p> This function gets the state of an AdmData&#8217;s protected flag. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> The AdmData which we want to check for the protected flag.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> TRUE if the given AdmData element is protected, FALSE otherwise.</dl>
<h3>int AdmData_setProtected (<code>AdmData</code> * data, int state, <code>AdmError</code> ** error)</h3>
<p> AdmData_setProtected: Set an AdmData&#8217;s protected flag. </p>
<p> This function sets the protected flag of an AdmData element to the value passed. </p>
<p> It will not set the flag of the root node, and is an error to attempt it. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> The AdmData of which we want to set the protected flag.<br />
 <i>state</i> The new protection state of the AdmData element.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 on error, 0 on success</dl>
<h3>int AdmList_isAnonymous (<code>AdmList</code> * list, <code>AdmError</code> ** error)</h3>
<p> AdmList_isAnonymous: Get the state of an AdmList&#8217;s anonymous flag. </p>
<p> This function gets the state of an AdmList&#8217;s anonymous flag. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>list</i> The AdmList which we want to check for the anonymous flag.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> TRUE if the given AdmList element is anonymous, FALSE otherwise.</dl>
<h3>int AdmList_setAnonymous (<code>AdmList</code> * list, int state, <code>AdmError</code> ** error)</h3>
<p> AdmList_setAnonymous: Set an AdmList&#8217;s anonymous flag. </p>
<p> This function sets the anonymous flag of an AdmList element to the value passed. It will not allow the flag to be cleared if it will cause a name collide, and will raise an error. </p>
<p> It will not set the flag of the root node, and is an error to attempt it. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>list</i> The AdmList of which we want to set the anonymous flag.<br />
 <i>state</i> The new anonymous state of the AdmList element.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 on error, 0 on success</dl>
<h3>int AdmList_isAtomic (<code>AdmList</code> * list, <code>AdmError</code> ** error)</h3>
<p> AdmList_isAtomic: Get the state of an AdmList&#8217;s atomic flag. </p>
<p> This function gets the state of an AdmList&#8217;s atomic flag. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>list</i> The AdmList which we want to check for the atomic flag.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> TRUE if the given AdmList element is atomic, FALSE otherwise.</dl>
<h3>int AdmList_setAtomic (<code>AdmList</code> * list, int state, <code>AdmError</code> ** error)</h3>
<p> AdmList_setAtomic: Set an AdmList&#8217;s atomic flag. </p>
<p> This function sets the atomic flag of an AdmList element to the value passed. </p>
<p> It will not set the flag of the root node, and is an error to attempt it. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>list</i> The AdmList of which we want to set the atomic flag.<br />
 <i>state</i> The new atomic state of the AdmList element.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 on error, 0 on success</dl>
<h3>int AdmList_isPrepend (<code>AdmList</code> * list, <code>AdmError</code> ** error)</h3>
<p> AdmList_isPrepend: Get the state of an AdmList&#8217;s prepend flag. </p>
<p> This function gets the state of an AdmList&#8217;s prepend flag. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>list</i> The AdmList which we want to check for the prepend flag.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> TRUE if the given AdmList element is prepend, FALSE otherwise.</dl>
<h3>int AdmList_setPrepend (<code>AdmList</code> * list, int state, <code>AdmError</code> ** error)</h3>
<p> AdmList_setPrepend: Set an AdmList&#8217;s prepend flag. </p>
<p> This function sets the prepend flag of an AdmList element to the value passed. </p>
<p> It will not set the flag of the root node, and is an error to attempt it. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>list</i> The AdmList of which we want to set the prepend flag.<br />
 <i>state</i> The new prepend state of the AdmList element.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 on error, 0 on success</dl>
<h3>unsigned int AdmList_getNumData (<code>AdmList</code> * list, <code>AdmError</code> ** error)</h3>
<p> AdmList_getNumData: Get the size of an AdmList&#8217;s child set. </p>
<p> This function gets the number of children held in an AdmList&#8217;s child set. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>list</i> The AdmList which we want to count.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The number of children inside the given list.</dl>
<h3><code>AdmData</code>* AdmList_getDataByIndex (<code>AdmList</code> * list, unsigned int index, <code>AdmError</code> ** error)</h3>
<p> AdmList_getDataByIndex: Get a child of an AdmList element by its index. </p>
<p> This function seeks on an AdmList&#8217;s child set, and returns its index&#8217;th child. It is an error to seek on an index greater &gt;= the list length, since the first element is stored at index 0. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>list</i> The AdmList which we want to access.<br />
 <i>index</i> The index of the child we want to get.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The pointer to requested AdmData element of the list.</dl>
<h3><code>AdmData</code>* AdmList_getDataByName (<code>AdmList</code> * list, const char * name, <code>AdmError</code> ** error)</h3>
<p> AdmList_getDataByName: Get a child od an AdmList element by its name. </p>
<p> This function seeks againts an AdmList&#8217;s child set, and returns the first child whose name matches the search name. It raises a AdmError if no name is found. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>list</i> The AdmList which we want to access.<br />
 <i>name</i> The name of the child we want to get.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The pointer to requested AdmData element of the list.</dl>
<h3><code>AdmData</code>* AdmList_getDataByPath (<code>AdmList</code> * list, const char * path, <code>AdmError</code> ** error)</h3>
<p> AdmList_getDataByPath: Get a child od an AdmList element by its path. </p>
<p> This function seeks againts an AdmList&#8217;s child set, and returns the first child whose path matches the search path. It raises a AdmError if no path is found. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>list</i> The AdmList which we want to access.<br />
 <i>path</i> The data path of the child we want to get.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The pointer to requested AdmData element of the list.</dl>
<h3><code>AdmData</code>* AdmList_addData (<code>AdmList</code> * list, <code>AdmDataType</code> type, const char * name, <code>AdmError</code> ** error)</h3>
<p> AdmList_addData: add a new child to an AdmList element. </p>
<p> This function appends a new child of the given type and name to the end of the AdmList. It returns a pointer to the new AdmData element. Name collides in non-anonymous lists are errors. </p>
<p> Note that new AdmCopy elements will have the invalid reference &#8221; as their initial value, and must be changed. </p>
<p> The new child is refed, but the ref is owned by its AdmList element, and no ref is implied to the accessor. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>list</i> The AdmList to which we want to add a new child.<br />
 <i>type</i> The AdmData type of the new child to be added.<br />
 <i>name</i> The name of the new child to be added.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The pointer to the newly added AdmData element.</dl>
<h3>int AdmList_moveData (<code>AdmList</code> * list, <code>AdmData</code> * data, unsigned int index, <code>AdmError</code> ** error)</h3>
<p> AdmList_moveData: reposition an AdmData element in its containing AdmList. </p>
<p> This function extracts an AdmData element from its containing list, and then reinserts it at the index value passed. It is an error to give it an illegal index value. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>list</i> The AdmList which we want to move in.<br />
 <i>data</i> The AdmData pointer of the child we want to move.<br />
 <i>index</i> The index to where we want to move the child.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 on error, 0 on success</dl>
<h3><code>AdmData</code>* AdmList_copyData (<code>AdmList</code> * list, <code>AdmData</code> * data, <code>AdmError</code> ** error)</h3>
<p> AdmList_copyData: copy a AdmData element into an AdmList element. </p>
<p> This function recursively copies an AdmData tree from the passed data node, and inserts the result onto the end of the passed AdmList. It checks for name collides in Non-anonymous lists, and will not copy a root node; both are errors. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>list</i> The AdmList to append the data to.<br />
 <i>data</i> The AdmData element to recursively copy and append to the list.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The pointer to the newly copied and appended AdmData element.</dl>
<h3><code>AdmData</code>* AdmList_renameCopyData (<code>AdmList</code> * list, <code>AdmData</code> * data, const char * name, <code>AdmError</code> ** error)</h3>
<p> AdmList_renameCopyData: copy and rename an AdmData element into an AdmList element. </p>
<p> This function recursively copies an AdmData tree from the passed data node, and inserts the result onto the end of the passed AdmList, using the specified name. It checks for name collides in Non-anonymous lists, and will not copy a root node; both are errors. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>list</i> The AdmList to append the data to.<br />
 <i>data</i> The AdmData element to recursively copy and append to the list.<br />
 <i>name</i> The new name to use.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The pointer to the newly copied and appended AdmData element.</dl>
<h3>unsigned int AdmData_getPos (<code>AdmData</code> * data, <code>AdmError</code> ** error)</h3>
<p> AdmData_getPos: Get the position of an AdmData node in its containing list. </p>
<p> This function returns the position that an AdmData node holds in its containing list. The position of the root node is defined to be 0. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> The AdmData of which we want to know the index.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The index of the data element in it&#8217;s parent list.</dl>
<h3>int AdmInt_getValue (<code>AdmInt</code> * int_scalar, <code>AdmError</code> ** error)</h3>
<p> Gets the integer value stored in an AdmInt node. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>int_scalar</i> a pointer to an AdmInt node<br />
 <i>error</i> an optional pointer to an AdmError pointer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the value of the node</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>AdmInt</code> </p>
<p> <code>AdmError</code></dl>
<h3>int AdmInt_setValue (<code>AdmInt</code> * int_scalar, int value, <code>AdmError</code> ** error)</h3>
<p> Sets the integer value stored in an AdmInt node. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>int_scalar</i> a pointer to an AdmInt node<br />
 <i>value</i> the integer value to set the node to<br />
 <i>error</i> an optional pointer to an AdmError pointer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 on error, 0 on success</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>AdmInt</code> </p>
<p> <code>AdmError</code></dl>
<h3>double AdmFloat_getValue (<code>AdmFloat</code> * float_scalar, <code>AdmError</code> ** error)</h3>
<p> Gets the double value stored in an AdmFloat node. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>float_scalar</i> a pointer to an AdmFloat node<br />
 <i>error</i> an optional pointer to an AdmError pointer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the double value of the node</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>AdmFloat</code> </p>
<p> <code>AdmError</code></dl>
<h3>int AdmFloat_setValue (<code>AdmFloat</code> * float_scalar, double value, <code>AdmError</code> ** error)</h3>
<p> Sets the double value stored in an AdmFloat node. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>float_scalar</i> a pointer to an AdmFloat element<br />
 <i>value</i> the double value to set the node with<br />
 <i>error</i> an optional pointer to an AdmError pointer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 on error, 0 on success</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>AdmFloat</code> </p>
<p> <code>AdmError</code></dl>
<h3>int AdmBool_getValue (<code>AdmBool</code> * bool_scalar, <code>AdmError</code> ** error)</h3>
<p> Gets the boolean value stored in an AdmBool node. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>bool_scalar</i> a pointer to an AdmBool node<br />
 <i>error</i> an optional pointer to an AdmError pointer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the value of the node as an int</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>AdmBool</code> </p>
<p> <code>AdmError</code></dl>
<h3>int AdmBool_setValue (<code>AdmBool</code> * bool_scalar, int value, <code>AdmError</code> ** error)</h3>
<p> Sets the boolean value stored in an AdmBool node. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>bool_scalar</i> a pointer to an AdmBool node<br />
 <i>value</i> the value to set the node to as an int<br />
 <i>error</i> an optional pointer to an AdmError pointer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 on error, 0 on success</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>AdmBool</code> </p>
<p> <code>AdmError</code></dl>
<h3><code>AdmRefStr</code>* AdmString_getValue (<code>AdmString</code> * string_scalar, <code>AdmError</code> ** error)</h3>
<p> Get the value of an AdmString element. </p>
<p> This function is used to request the string stored in an AdmString element. The string returned must be considered const and volatile, and if it is needed for long periods of time, the programmer should copy it. </p>
<p> Specifically, it is guaranteed for only so long as the AdmString element remains refed, and its value is not changed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>string_scalar</i> The pointer to the AdmString element<br />
 <i>error</i> optional pointer to an AdmError pointer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An AdmRefStr with the AdmString element&#8217;s value string.</dl>
<h3>int AdmString_setValue (<code>AdmString</code> * string_scalar, const char * value, <code>AdmError</code> ** error)</h3>
<p> Set the value of an AdmString element. </p>
<p> This function is used to set the value of an AdmString element. It stores a copy of the value string it is passed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>string_scalar</i> The pointer to the AdmString element.<br />
 <i>value</i> The pointer to the string.<br />
 <i>error</i> optional pointer to an AdmError pointer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 on error, 0 on success</dl>
<h3><code>AdmRefStr</code>* AdmBase64_getValue (<code>AdmBase64</code> * base64_scalar, <code>AdmError</code> ** error)</h3>
<p> AdmBase64_getValue: Get the value of an AdmBase64 element : a pointer to an AdmBase64 element : an optional AdmError </p>
<p> This function is used to request the string stored in an AdmBase64 string element. The string returned must be considered const and volatile, and if it is needed for long periods of time, the programmer should copy it. </p>
<p> Return value: a pointer to the AdmBase64 element&#8217;s value string.</p>
<h3>int AdmBase64_setValue (<code>AdmBase64</code> * base64_scalar, const char * value, <code>AdmError</code> ** error)</h3>
<p> This function is used to set the value of an AdmBase64 string element. It stores a copy of the value string it is passed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>base64_scalar</i> a pointer to an AdmBase64 element<br />
 <i>value</i> a pointer to a base64 encoded binary string<br />
 <i>error</i> an optional AdmError</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 on error, 0 on success</dl>
<h3>size_t AdmBase64_getBinValue (<code>AdmBase64</code> * base64_scalar, void ** value, <code>AdmError</code> ** error)</h3>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>base64_scalar</i> a pointer to an AdmBase64 element<br />
 <i>value</i> a pointer to a void pointer to return the address of the new buffer.<br />
 <i>error</i> an optional AdmError</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the size of the new buffer.</dl>
<p> This function will decode and return a copy of the binary string stored in a AdmBase64 element. You must free the returned buffer. </p>
<p> Return value: a pointer to the AdmBase64 element&#8217;s value string.</p>
<h3>int AdmBase64_setBinValue (<code>AdmBase64</code> * base64_scalar, const void * value, size_t size, <code>AdmError</code> ** error)</h3>
<p> This function is used to set the binary value of an AdmBase64 string element. It stores an encoded copy of the value string it is passed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>base64_scalar</i> a pointer to an AdmBase64 element<br />
 <i>value</i> a pointer to a binary string<br />
 <i>size</i> the size of the binary string<br />
 <i>error</i> an optional AdmError</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 on error, 0 on success</dl>
<h3><code>AdmRefStr</code>* AdmCopy_getValue (<code>AdmCopy</code> * copy_scalar, <code>AdmError</code> ** error)</h3>
<p> This function is used to request the path of an AdmCopy element. The string returned must be considered const and volatile, and if it is needed for long periods of time, the programmer should copy it. </p>
<p> Specifically, it is guranteed for only so long as the AdmCopy element is refed, and its value is not changed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>copy_scalar</i> a pointer to an AdmCopy element<br />
 <i>error</i> an optional GError</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An AdmRefStr containing the AdmCopy&#8217;s path</dl>
<h3>int AdmCopy_setValue (<code>AdmCopy</code> * copy_scalar, const char * value, <code>AdmError</code> ** error)</h3>
<p> This function is used to set the path of an AdmCopy element. It stores a copy of the string passed to it, after checking its path validity. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>copy_scalar</i> a pointer to an AdmCopy element<br />
 <i>value</i> a pointer to a valid path string<br />
 <i>error</i> an optional GError</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 on error, 0 on success</dl>
<h3><code>AdmRefStr</code>* AdmBlackBox_getCacheDir (<code>AdmError</code> ** error)</h3>
<p> Gets the cache directory the alchemist is currently using. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> an optional pointer to an AdmError pointer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the cache dir</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> you do not own the return stritg, and must not free it</dl>
<h3>int AdmBlackBox_setCacheDir (const char * path, <code>AdmError</code> ** error)</h3>
<p> Sets the cache directory the alchemist is currently using. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>path</i> the cache directory you want to use<br />
 <i>error</i> an optional pointer to an AdmError pointer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 on failure, 0 on succes</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> passing NULL as the path resets the path to the default</dl>
<h3><code>AdmBlackBox</code>* AdmBlackBox_getBox (<code>AdmList</code> * box_cfg, <code>AdmError</code> ** error)</h3>
<h3><code>adm_bb_cap_t</code> AdmBlackBox_caps (<code>AdmBlackBox</code> * box, <code>AdmError</code> ** error)</h3>
<p> Returns a capability vector listing the capabilities of an AdmBlackBox. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>box</i> The AdmBlackBox to check<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> an <code>adm_bb_cap_t</code> structure</dl>
<h3>void AdmBlackBox_ref (<code>AdmBlackBox</code> * box, <code>AdmError</code> ** error)</h3>
<p> Increase reference to given AdmBlackBox element. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>box</i> The AdmBlackBox to increase the reference to.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<h3>void AdmBlackBox_unref (<code>AdmBlackBox</code> * box, <code>AdmError</code> ** error)</h3>
<p> Decrease reference to given AdmBlackBox element. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>box</i> The AdmBlackBox to decrease the reference to.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<h3><code>AdmContext</code>* AdmBlackBox_read (<code>AdmBlackBox</code> * box, <code>AdmError</code> ** error)</h3>
<p> Tries to read the most current context from the given AdmBlackBox and return it. The BlackBox may not be able to be readable in which case NULL will be returned. Also it may allow caching and do so transparently. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>box</i> The AdmBlackBox to read from.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The pointer to the AdmContext retrived through the given box.</dl>
<h3>int AdmBlackBox_listSerial (<code>AdmBlackBox</code> * box, unsigned int * array, unsigned int array_len, unsigned int top_serial, <code>AdmError</code> ** error)</h3>
<p> Creates a list of serial numbers of the given AdmBlackBox subject to the constraints. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>box</i> The AdmBlackBox to get the list of serial numbers from.<br />
 <i>array</i> The pointer to the preallocated array of int values to be filled with the serial numbers.<br />
 <i>array_len</i> The size of the perallocated array.<br />
 <i>top_serial</i> The highest serial number that we request. Only serial numbers below that will be returned. Use 0 to request the newest (highest) serial numbers.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The amount of serial numbers filled in. Always less or equal to the array length.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The list of serial numbers can partially come from the local cached BlackBoxes as well.</dl>
<h3><code>AdmContext</code>* AdmBlackBox_readSerial (<code>AdmBlackBox</code> * box, unsigned int serial, <code>AdmError</code> ** error)</h3>
<p> Reads a context from the given AdmBlackBox with the specified serial number. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>box</i> The AdmBlackBox to read the context from.<br />
 <i>serial</i> The serial number of the context we request.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The pointer to the AdmContext retrived through the given box or NULL if no context with that serial number exists.</dl>
<h3>int AdmBlackBox_write (<code>AdmBlackBox</code> * box, <code>AdmContext</code> * context, <code>AdmError</code> ** error)</h3>
<p> Write the given AdmContext to the given AdmBlackBox. Does automatic caching if the given AdmBlackBox supports it. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>box</i> The AdmBlackBox to write to.<br />
 <i>context</i> The AdmContext to be written to the box.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, all other values indicate an error.</dl>
<h3>unsigned int AdmBlackBox_getMark (<code>AdmBlackBox</code> * box, const char * mark, <code>AdmError</code> ** error)</h3>
<p> Get the serial number of the given AdmBlackBox for the given mark. The whole business with marks allows us to &#8216;tag&#8217; cached boxes and to identify if they are dirty or not. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>box</i> The AdmBlackBox from which to get the marked serial.<br />
 <i>mark</i> The mark string.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The serial number of the marked cached box or 0 if no marked cached box exists.</dl>
<h3>int AdmBlackBox_setMark (<code>AdmBlackBox</code> * box, const char * mark, <code>AdmError</code> ** error)</h3>
<p> Mark the given AdmBlackBox. The serial number is extracted from the given AdmBlackBox automatically. Any existing mark will be overwritten. If an AdmBlackBox is cached, then it is possible to mark it. This provides a mechanism for marking the top serial number in the cache down at a given mark, which is a string; allowing various applications to check to see if an interface has changed since the last time the accessed by doing something along the lines of: </p>
<pre><code>
AdmBlackBox_setMark(box_p, 'app1_mark_string', error);
... int i;
 if ((AdmBlackBok_listSerial(box_p, &amp;i, 1, 0, NULL) &amp;&amp;
        (i != AdmBlackBox_getMark(box_p, 'app1_mark_string', NULL)) {
    ...
 }
</code></pre>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>box</i> The AdmBlackBox which we want to mark.<br />
 <i>mark</i> The mark string.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, all other values indicate an error.</dl>
<h3>int AdmBlackBox_clearMark (<code>AdmBlackBox</code> * box, const char * mark, <code>AdmError</code> ** error)</h3>
<p> Clear the mark for the given AdmBlackBox. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>box</i> The AdmBlackBox where we want to clear its mark.<br />
 <i>mark</i> The mark string.<br />
 <i>error</i> Optional pointer to AdmError pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, all other values indicate an error.</dl>
<h3><code>AdmRefStr</code>* AdmSwitchboard_getSwbDir (<code>AdmError</code> ** error)</h3>
<p> Gets the swb directory the alchemist is currently using. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> an optional pointer to an AdmError pointer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the swb dir</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> you do not own the return stritg, and must not free it</dl>
<h3>int AdmSwitchboard_setSwbDir (const char * path, <code>AdmError</code> ** error)</h3>
<p> Sets the swb directory the alchemist is currently using. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>path</i> the swb directory you want to use<br />
 <i>error</i> an optional pointer to an AdmError pointer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 on failure, 0 on succes</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> passing NULL as the path resets the path to the default</dl>
<h3>int AdmSwitchboard_markNsp (const char * namespace, const char * subspace, const char * mark, <code>AdmError</code> ** error)</h3>
<h3>int AdmSwitchboard_markNspWithConfig (<code>AdmList</code> * namespace_cfg, const char * subspace, const char * mark, <code>AdmError</code> ** error)</h3>
<h3>int AdmSwitchboard_checkNspMark (const char * namespace, const char * subspace, const char * mark, <code>AdmError</code> ** error)</h3>
<h3>int AdmSwitchboard_checkNspMarkWithConfig (<code>AdmList</code> * namespace_cfg, const char * subspace, const char * mark, <code>AdmError</code> ** error)</h3>
<h3><code>AdmContext</code>* AdmSwitchboard_readNsp (const char * namespace, const char * subspace, unsigned int depth, <code>AdmError</code> ** error)</h3>
<p> read the given subspace from the given namespace </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>namespace</i> the namespace to read<br />
 <i>subspace</i> the box set to extract, NULL uses the default &#8216;config&#8217; set<br />
 <i>depth</i> the number of boxes in the namespace to read, 0 means all.<br />
 <i>error</i> an optional pointer to an AdmError pointer</dl>
<h3><code>AdmContext</code>* AdmSwitchboard_readNspWithConfig (<code>AdmList</code> * namespace_cfg, const char * subspace, unsigned int depth, <code>AdmError</code> ** error)</h3>
<h3>int AdmSwitchboard_writeNsp (const char * namespace, const char * subspace, <code>AdmContext</code> * context, <code>AdmError</code> ** error)</h3>
<p> writes the given subspace in the given namespace </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>namespace</i> the namespace to write<br />
 <i>subspace</i> the box set to extract, NULL uses the default &#8216;config&#8217; set<br />
 <i>context</i> the context to write<br />
 <i>error</i> an optional pointer to an AdmError pointer</dl>
<h3>int AdmSwitchboard_writeNspWithConfig (<code>AdmList</code> * namespace_cfg, const char * subspace, <code>AdmContext</code> * context, <code>AdmError</code> ** error)</h3>
<h3><code>AdmContext</code>* AdmSwitchboard_readNspCtx (const char * namespace, <code>AdmError</code> ** error)</h3>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>namespace</i> the name of the namespace to read<br />
 <i>error</i> an optional pointer to an AdmError pointer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> an AdmContext that is the namespace configuration</dl>
<h3>int AdmSwitchboard_writeNspCtx (const char * namespace, <code>AdmContext</code> * namespace_ctx, int mode, uid_t uid, gid_t gid, <code>AdmError</code> ** error)</h3>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>namespace</i> the name of the namespace to read<br />
 <i>context</i> the configuration context to write<br />
 <i>mode</i> the file mode to write the context out with<br />
 <i>uid</i> the uid to write the file with, -1 for dont care<br />
 <i>gid</i> the gid to write the file with, -1 for dont care<br />
 <i>error</i> an optional pointer to an AdmError pointer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 on failure, 0 on succes</dl>
<h3><code>AdmList</code>* AdmSwitchboard_getNspCfg (<code>AdmContext</code> * namespace_ctx, const char * namespace, <code>AdmError</code> ** error)</h3>
<p> extract a namespace config from a namespace context </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>namespace</i> the namespace to extract<br />
 <i>config</i> the namespace config context</dl>
<h3><code>AdmList</code>* AdmSwitchboard_getSubspCfg (<code>AdmList</code> * namespace_cfg, const char * subspace, <code>AdmError</code> ** error)</h3>
<p> extract a box set from a namespace config </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>subspace</i> the box set to extract, NULL uses the default &#8216;config&#8217; set<br />
 <i>namespace</i> the namespace used<br />
 <i>config</i> the namespace config context</dl>
<h3><code>AdmBlackBox</code>* AdmSwitchboard_getBox (<code>AdmList</code> * subspace_cfg, const char * box_name, <code>AdmError</code> ** error)</h3>
<p> extract a box_config set from a namespace config </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>box_name</i> the box to extract<br />
 <i>subspace_cfg</i> the subspace config no use</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Alchemist from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbCP">Enumeration Type Documentation</a></p>
<dd>
<dt><a href="#lbCR">Function Documentation</a></p>
<dd>
<dt><a href="#lbHA">Author</a></p>
<dd></dl>
