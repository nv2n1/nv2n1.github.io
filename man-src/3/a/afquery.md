---
title: "afquery(3)"
name: "afquery"
section: "3"
letter: "a"
url: "/docs/linux/man/3-afquery/"
---

afQuery, afQueryLong, afQueryDouble, afQueryPointer - query the capabilities of the Audio File Library 

<h2>Synopsis</h2><pre>#include &lt;audiofile.h&gt;</pre><pre>AUpvlist afQuery (int querytype, int arg1, int arg2, int arg3, int arg4);</pre><pre>long afQueryLong (int querytype, int arg1, int arg2, int arg3, int arg4);</pre><pre>double afQueryDouble (int querytype, int arg1, int arg2, int arg3,
 int arg4);</pre><pre>void *afQueryPointer (int querytype, int arg1, int arg2, int arg3,
 int arg4);</pre><h2>Parameters</h2><i>querytype</i> can be one of the following: 

<dl COMPACT><dd>&bull; 

 AF_QUERYTYPE_FILEFMT</dl><dl COMPACT><dd>&bull; 

 AF_QUERYTYPE_INST</dl><dl COMPACT><dd>&bull; 

 AF_QUERYTYPE_INSTPARAM</dl><dl COMPACT><dd>&bull; 

 AF_QUERYTYPE_COMPRESSION</dl><dl COMPACT><dd>&bull; 

 AF_QUERYTYPE_COMPRESSIONPARAM</dl><dl COMPACT><dd>&bull; 

 AF_QUERYTYPE_MISC</dl><dl COMPACT><dd>&bull; 

 AF_QUERYTYPE_MARK</dl><dl COMPACT><dd>&bull; 

 AF_QUERYTYPE_LOOP</dl>
 

 <i>arg1</i>, <i>arg2</i>, <i>arg3</i>, and <i>arg4</i> are integer selectors whose meaning depends upon <i>querytype</i>.
<h2>Return Value</h2>Upon success, afQuery will return a non-null AUpvlist value. Upon failure, afQuery will return null while afQueryLong and afQueryDouble will return -1 and afQueryPointer will return null. 

 Pointers representing character strings are owned by the Audio File Library and must not be freed; all other pointer values must be freed by the caller.
<h2>Description</h2>For AF_QUERYTYPE_FILEFMT, the following selectors are valid values for <i>arg1</i>: 

 AF_QUERY_LABEL
<dl COMPACT><dd>Request a short label string for the format (e.g., &quot;aiff&quot;).</dl>
 

 AF_QUERY_NAME
<dl COMPACT><dd>Request a short name for the format (e.g., &quot;MS RIFF WAVE&quot;).</dl>
 

 AF_QUERY_DESC
<dl COMPACT><dd>Request a descriptive name for the format (e.g., &quot;Audio Interchange File Format&quot;).</dl>
 

 AF_QUERY_IMPLEMENTED
<dl COMPACT><dd>Request a boolean value indicating whether the format is implemented for reading and writing in the Audio File Library.</dl>
 

 AF_QUERY_ID_COUNT
<dl COMPACT><dd>Request the total number of formats implemented.</dl>
 

 AF_QUERY_IDS
<dl COMPACT><dd>Request an integer array of the id token values of all implemented file formats.</dl>
 

 AF_QUERY_COMPRESSION_TYPES
<dl COMPACT><dd>Used with the selector AF_QUERY_VALUE_COUNT in <i>arg2</i>, this will return a long integer containing the number of compression schemes available for use within the format specified in <i>arg3</i>. Used with selector AF_QUERY_VALUES, it returns a pointer to an integer array containing the compression id values of the compression schemes supported by the format specified in <i>arg3</i>.</dl>
 

 AF_QUERY_SAMPLE_FORMATS
<dl COMPACT><dd>Used with the selector AF_QUERY_DEFAULT in <i>arg2</i>, this will return the default sample format for the file format specified in <i>arg3</i>.</dl>
 

 AF_QUERY_SAMPLE_SIZES
<dl COMPACT><dd>Used with selector AF_QUERY_DEFAULT in <i>arg2</i>, this will return the default sample width for the file format specified in <i>arg3</i>.</dl>
 

 For AF_QUERYTYPE_INST, the following selectors are valid for <i>arg1</i>: 

 AF_QUERY_SUPPORTED
<dl COMPACT><dd>Request a boolean value indicating whether the file format in <i>arg2</i> supports instruments.</dl>
 

 AF_QUERY_MAX_NUMBER
<dl COMPACT><dd>Request an integer value indicating the maximum number of instruments supported by the file format in <i>arg2</i>.</dl>
 

 For AF_QUERYTYPE_INSTPARAM, the following selectors are valid for <i>arg1</i>: 

 AF_QUERY_SUPPORTED
<dl COMPACT><dd>Request a boolean value indicating whether the file format in <i>arg2</i> supports instrument parameters.</dl>
 

 AF_QUERY_ID_COUNT
<dl COMPACT><dd>Request an integer value indicating the number of instrument parameters supported by the file format in <i>arg2</i>.</dl>
 

 AF_QUERY_IDS
<dl COMPACT><dd>Request an integer array containing the instrument parameter values for the file format in <i>arg2</i>.</dl>
 

 AF_QUERY_TYPE
<dl COMPACT><dd>For the file format in <i>arg2</i>, request the type of the instrument parameter in <i>arg3</i>.</dl>
 

 AF_QUERY_NAME
<dl COMPACT><dd>For the file format in <i>arg2</i>, request the name of the instrument parameter in <i>arg3</i>.</dl>
 

 AF_QUERY_DEFAULT
<dl COMPACT><dd>For the file format in <i>arg2</i>, request the default value of the instrument parameter in <i>arg3</i>.</dl><h2>Errors</h2>afQuery can produce the following errors: 

 AF_BAD_QUERYTYPE
<dl COMPACT><dd>The query type is unsupported.</dl>
 

 AF_BAD_QUERY
<dl COMPACT><dd>The arguments to the query are bad.</dl><h2>Author</h2>Michael Pruett &lt;michael [at] 68k.org&gt;
