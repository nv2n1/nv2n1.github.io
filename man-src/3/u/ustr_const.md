---
title: "ustr_const(3)"
name: "ustr_const"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustr_const/"
description: "ustr_const – ustr string library constants"
---

<p>ustr_const &#8211; ustr string library constants</p>
<h2>Synopsis</h2>
<pre><code>#include &quot;ustr.h&quot;
</code></pre>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_CONF_INCLUDE_CODEONLY_HEADERS</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_CONF_USE_EOS_MARK</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_CONF_USE_ASSERT</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_CONF_COMPILE_USE_ATTRIBUTES</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_CONF_COMPILE_TYPEDEF</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_CONF_COMPILE_USE_INLINE</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_BEG_CONST1</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_BEG_CONST2</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_BEG_CONST4</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_BEG_FIXED1</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_BEG_FIXED2</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_BEG_FIXED4</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_BEG_FIXED8</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_END_ALOCDx</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_END_CONSTx</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_END_FIXEDx</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_FLAG_PARSE_NUM_DEF</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_FLAG_PARSE_NUM_SEP</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_FLAG_PARSE_NUM_OVERFLOW</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_FLAG_PARSE_NUM_SPACE</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_FLAG_PARSE_NUM_NO_BEG_ZERO</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_FLAG_PARSE_NUM_NO_BEG_PM</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_FLAG_PARSE_NUM_NO_NEGATIVE</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_FLAG_PARSE_NUM_EXACT</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_TYPE_PARSE_NUM_ERR_NONE</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_TYPE_PARSE_NUM_ERR_ONLY_S</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_TYPE_PARSE_NUM_ERR_ONLY_SPM</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_TYPE_PARSE_NUM_ERR_ONLY_SPMX</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_TYPE_PARSE_NUM_ERR_OOB</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_TYPE_PARSE_NUM_ERR_OVERFLOW</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_TYPE_PARSE_NUM_ERR_NEGATIVE</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_TYPE_PARSE_NUM_ERR_BEG_ZERO</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_FLAG_SPLIT_DEF</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_FLAG_SPLIT_RET_SEP</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_FLAG_SPLIT_RET_NON</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_FLAG_SPLIT_KEEP_CONFIG</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_NULL</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_POOL_NULL</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_TRUE</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_FALSE</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_CNTL_OPT_GET_REF_BYTES</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_CNTL_OPT_SET_REF_BYTES</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_CNTL_OPT_GET_HAS_SIZE</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_CNTL_OPT_SET_HAS_SIZE</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_CNTL_OPT_GET_EXACT_BYTES</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_CNTL_OPT_SET_EXACT_BYTES</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_CNTL_OPT_GET_MEM</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_CNTL_OPT_SET_MEM</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_CNTL_OPT_GET_MC_M_SCRUB</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_CNTL_OPT_SET_MC_M_SCRUB</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_CNTL_OPT_GET_MC_F_SCRUB</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_CNTL_OPT_SET_MC_F_SCRUB</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_CNTL_OPT_GET_MC_R_SCRUB</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_CNTL_OPT_SET_MC_R_SCRUB</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_CNTL_OPT_GET_FMT</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_CNTL_OPT_SET_FMT</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_POOL_LL_CNTL_GET_FREE_CMP</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_POOL_LL_CNTL_SET_FREE_CMP</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_POOL_LL_CNTL_GET_REALLOC</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <code>USTR_POOL_LL_CNTL_SET_REALLOC</code> </p>
<p> <code>Constant: </code> USTR_CONF_INCLUDE_CODEONLY_HEADERS<br />
 <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This switch controls whether all the code will be included as inline functions. Having this be non-zero means that you don&#8217;t have to link against the library.<br />
 <code>Constant: </code> USTR_CONF_USE_EOS_MARK<br />
 <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This switch turns on End of String markers, so any bounds overflow will be noticed by ustr_assert_valid(). <code>Note:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Changing this will not do anything useful unless USTR_CONF_INCLUDE_CODEONLY_HEADERS is non-zero.<br />
 <code>Constant: </code> USTR_CONF_USE_ASSERT<br />
 <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This switch turns USTR_ASSERT()&nbsp;<wbr>calls on, so the code within them will be evaluated. Note that there are many calls to ustr_assert_valid()&nbsp;<wbr>within USTR_ASSERT()&nbsp;<wbr>macros and that call is relatively expensive. <code>Note:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Changing this will not do anything useful unless USTR_CONF_INCLUDE_CODEONLY_HEADERS is non-zero.<br />
 <code>Constant: </code> USTR_CONF_COMPILE_USE_ATTRIBUTES<br />
 <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This switch controls whether gcc type&nbsp;<wbr>__attribute__()&nbsp;<wbr>statements are used in the public headers headers for the library. If the value is 1 then if they are supported by the compiler that built the library they will be used, if the value is 0 they won&#8217;t be used at all.<br />
 <code>Constant: </code> USTR_CONF_COMPILE_TYPEDEF<br />
 <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This switch controls whether typedef will be used for the structs in the public headers for the library. If the value is 1 then they will be used, if the value is 0 they won&#8217;t be used at all&nbsp;<wbr>(and your code will have to use struct tags instead &#8212; note all libraries using ustr should compile without this option set).<br />
 <code>Constant: </code> USTR_CONF_COMPILE_USE_INLINE<br />
 <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This switch controls whether inline functions will be used in a few cases where the function bodies are very small. <code>Note:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>In some cases this is used so that GCC can eliminate calls to strlen(), for the&nbsp;<wbr>*_cstr()&nbsp;<wbr>functions. </p>
<h2>Constants to created fixed/read-only Ustr&#8217;s</h2>
<p><code>Constant: </code> USTR_BEG_CONST1 </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This macro is a constant C-style string of the first byte of a constant/read-only Ustr that has a length in the range 0-255. </p>
<p> <code>Constant: </code> USTR_BEG_CONST2 </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This macro is a constant C-style string of the first byte of a constant/read-only Ustr that has a length in the range 0-65535. </p>
<p> <code>Constant: </code> USTR_BEG_CONST4 </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This macro is a constant C-style string of the first byte of a constant/read-only Ustr that has a length in the range 0-4294967295. </p>
<p> <code>Constant: </code> USTR_BEG_FIXED1 </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This macro is a constant C-style string of the first byte of a fixed Ustr that has a length in the range 0-255. </p>
<p> <code>Constant: </code> USTR_BEG_FIXED2 </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This macro is a constant C-style string of the first byte of a fixed Ustr that has a length in the range 0-65535. </p>
<p> <code>Constant: </code> USTR_BEG_FIXED4 </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This macro is a constant C-style string of the first byte of a fixed Ustr that has a length in the range 0-4294967295. </p>
<p> <code>Constant: </code> USTR_BEG_FIXED8 </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This macro is a constant C-style string of the first byte of a fixed Ustr that has a length in the range 0-18446744073709551615. </p>
<p> <code>Note:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This macro is only available if the Ustr code was compiled in a 64bit environment. </p>
<p> <code>Constant: </code> USTR_END_ALOCDx </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This macro is a constant C-style string of the last bytes of an allocated Ustr. </p>
<p> <code>Note:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Unless USTR_CONF_USE_EOS_MARK is non-zero, this is just the NIL byte. </p>
<p> <code>Constant: </code> USTR_END_CONSTx </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This macro is a constant C-style string of the last bytes of a constant/read-only Ustr. </p>
<p> <code>Note:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Unless USTR_CONF_USE_EOS_MARK is non-zero, this is just the NIL byte. </p>
<p> <code>Constant: </code> USTR_END_FIXEDx </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This macro is a constant C-style string of the last bytes of a fixed Ustr. </p>
<p> <code>Note:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Unless USTR_CONF_USE_EOS_MARK is non-zero, this is just the NIL byte.</p>
<h2>Constants to use with parsing numbers: ustr_parse_uintmaxx, etc.</h2>
<p><code>Constant: </code> USTR_FLAG_PARSE_NUM_DEF </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Default flags, this is merely 0 but can be used as live documentation. </p>
<p> <code>Constant: </code> USTR_FLAG_PARSE_NUM_SEP </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This flag allows the parsing&nbsp;<wbr>(and ignoring)&nbsp;<wbr>of the seperator character, at arbitrary pointers in the number, so&nbsp;<wbr>&quot;1234&quot;&nbsp;<wbr>and&nbsp;<wbr>&quot;1_234&quot;&nbsp;<wbr>would both parse the same&nbsp;<wbr>(assuming&nbsp;<wbr>&quot;_&quot;&nbsp;<wbr>is the seperator). </p>
<p> <code>Constant: </code> USTR_FLAG_PARSE_NUM_OVERFLOW </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This flag turns on the overflow checking, in other words without it USTR_TYPE_PARSE_NUM_ERR_OVERFLOW will never be returned as an error code. </p>
<p> <code>Constant: </code> USTR_FLAG_PARSE_NUM_SPACE </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This flag allows one or more&nbsp;<wbr>&#8216;&nbsp;<wbr>&#8216;&nbsp;<wbr>(Space)&nbsp;<wbr>characters before the number or number prefix&nbsp;<wbr>(Plus Sign, Hyphen). </p>
<p> <code>Note:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Other forms of whitespace don&#8217;t count, this just affects&nbsp;<wbr>&#8216;&nbsp;<wbr>&#8216;. </p>
<p> <code>Constant: </code> USTR_FLAG_PARSE_NUM_NO_BEG_ZERO </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This flag disallows one or more&nbsp;<wbr>&#8216;0&#8217;&nbsp;<wbr>(Digit Zero)&nbsp;<wbr>characters before the number. </p>
<p> <code>Constant: </code> USTR_FLAG_PARSE_NUM_NO_BEG_PM </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This flag disallows a plus or a minus character before the number. </p>
<p> <code>Constant: </code> USTR_FLAG_PARSE_NUM_NO_NEGATIVE </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This flag disallows negative values. </p>
<p> <code>Constant: </code> USTR_FLAG_PARSE_NUM_EXACT </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This flag makes the parsing functions return an error if the entire string doesn&#8217;t contain the number being parsed. </p>
<p> <code>Constant: </code> USTR_TYPE_PARSE_NUM_ERR_NONE </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This error code has the value 0, and means that no error occurred parsing the number. </p>
<p> <code>Constant: </code> USTR_TYPE_PARSE_NUM_ERR_ONLY_S </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This error code means that the Ustr string consisted only of spaces. </p>
<p> <code>Constant: </code> USTR_TYPE_PARSE_NUM_ERR_ONLY_SPM </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This error code means that the Ustr string consisted only spaces, and a plus or minus sign. </p>
<p> <code>Constant: </code> USTR_TYPE_PARSE_NUM_ERR_ONLY_SPMX </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This error code means that the Ustr string consisted of only spaces, a plus or minus sign and a&nbsp;<wbr>&quot;0x&quot;&nbsp;<wbr>base 16 prefix.<br />
 <code>Constant: </code> USTR_TYPE_PARSE_NUM_ERR_OOB </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This error code means that the Ustr string had characters in it that where out of bounds from the working base. </p>
<p> <code>Note:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Without the USTR_FLAG_PARSE_NUM_EXACT, this error is ignored as soon as any number is parsed. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This out of bounds includes the Ustr string&nbsp;<wbr>&quot;++&quot;&nbsp;<wbr>as well as&nbsp;<wbr>&quot;4A&quot;, when parsing in a base less than 11. </p>
<p> <code>Constant: </code> USTR_TYPE_PARSE_NUM_ERR_OVERFLOW </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This error code means that the number parsed from the Ustr string would overflow the type it is being parsed into, this is only returned when the USTR_FLAG_PARSE_NUM_OVERFLOW flag was passed to the parse function. </p>
<p> <code>Constant: </code> USTR_TYPE_PARSE_NUM_ERR_NEGATIVE </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This error code means that the number parsed from the Vstr string starts with a&nbsp;<wbr>&#8216;-&#8216;&nbsp;<wbr>(Hyphen)&nbsp;<wbr>character when it is supposed to be an unsigned number. </p>
<p> <code>Constant: </code> USTR_TYPE_PARSE_NUM_ERR_BEG_ZERO </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This error code means that the number parsed from the Vstr string starts with a&nbsp;<wbr>&#8216;0&#8217;&nbsp;<wbr>(Digit Zero)&nbsp;<wbr>character, when the USTR_FLAG_PARSE_NUM_NO_BEG_ZERO flag was passed to the parse function.</p>
<h2>Constants to pass to ustr_split*</h2>
<p><code>Constant: </code> USTR_FLAG_SPLIT_DEF </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Default flags, this is merely 0 but can be used as live documentation. </p>
<p> <code>Constant: </code> USTR_FLAG_SPLIT_RET_SEP </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Return the separator along with the tokens. For example splitting&nbsp;<wbr>&quot;a,b,&quot;&nbsp;<wbr>using separator&nbsp;<wbr>&quot;,&quot;&nbsp;<wbr>will return the tokens&nbsp;<wbr>&quot;a,&quot;&nbsp;<wbr>and&nbsp;<wbr>&quot;b,&quot;&nbsp;<wbr>whereas without this flag only&nbsp;<wbr>&quot;a&quot;&nbsp;<wbr>and&nbsp;<wbr>&quot;b&quot;&nbsp;<wbr>would be returned. </p>
<p>&nbsp;<wbr>.br <code>Constant: </code> USTR_FLAG_SPLIT_RET_NON </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Return empty tokens. For example: splitting&nbsp;<wbr>&quot;a,,b&quot;&nbsp;<wbr>with separator&nbsp;<wbr>&quot;,&quot;&nbsp;<wbr>will return the tokens&nbsp;<wbr>{&quot;a&quot;&nbsp;<wbr>&quot;&quot;&nbsp;<wbr>&quot;b&quot;}.<br />
 <code>Constant: </code> USTR_FLAG_SPLIT_KEEP_CONFIG </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Force the returned Ustr&#8217;s to have same configuration parameters as the Ustr string that is being split.</p>
<h2>Misc constants to use in code</h2>
<p><code>Constant: </code> USTR_NULL </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This macro is merely 0 cast to&nbsp;<wbr>(struct Ustr&nbsp;<wbr>*), and can be used anywhere NULL would be but&nbsp;<wbr>&quot;returns&quot;&nbsp;<wbr>the correct type. </p>
<p> <code>Constant: </code> USTR_POOL_NULL </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This macro is merely 0 cast to&nbsp;<wbr>(struct Ustr_pool&nbsp;<wbr>*), and can be used anywhere NULL would be but&nbsp;<wbr>&quot;returns&quot;&nbsp;<wbr>the correct type. </p>
<p> <code>Constant: </code> USTR_TRUE </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This macro is 1, but shows the intent that a boolean value is expected and not a number. </p>
<p> <code>Constant: </code> USTR_FALSE </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This macro is 0, but shows the intent that a boolean value is expected and not a number.</p>
<h2>Constants passed to ustr_cntl_opt()</h2>
<p><code>Constant: </code> USTR_CNTL_OPT_GET_REF_BYTES </p>
<p> Parameter<code>[1]</code>: Number of bytes for default reference count in Ustr<br />
 Type<code>[1]</code>: size_t * </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This option will get the default number of bytes used for a reference count when creating Ustr&#8217;s. </p>
<p> <code>Constant: </code> USTR_CNTL_OPT_SET_REF_BYTES </p>
<p> Parameter<code>[1]</code>: Number of bytes for default reference count in Ustr<br />
 Type<code>[1]</code>: size_t </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This option will set the default number of bytes used for a reference count when creating Ustr&#8217;s. </p>
<p> <code>Note:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>For a single instance, the ustr_dupx_*()&nbsp;<wbr>functions can be used. </p>
<p> <code>Constant: </code> USTR_CNTL_OPT_GET_HAS_SIZE </p>
<p> Parameter<code>[1]</code>: Default flag for whether to include an explicit size in a Ustr<br />
 Type<code>[1]</code>: int * </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This option will get the default flag for whether to store an explicit size in created Ustr&#8217;s. </p>
<p> <code>Constant: </code> USTR_CNTL_OPT_SET_HAS_SIZE </p>
<p> Parameter<code>[1]</code>: Default flag for whether to include an explicit size in a Ustr<br />
 Type<code>[1]</code>: int </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This option will set the default flag for whether to store an explicit size in created Ustr&#8217;s. </p>
<p> <code>Note:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>For a single instance, the ustr_dupx_*()&nbsp;<wbr>functions can be used. </p>
<p> <code>Constant: </code> USTR_CNTL_OPT_GET_EXACT_BYTES </p>
<p> Parameter<code>[1]</code>: Default flag for whether to exactly allocate memory<br />
 Type<code>[1]</code>: int * </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This option will get the default flag for whether to exactly allocate memory when a Ustr needs to be resized. </p>
<p> <code>Constant: </code> USTR_CNTL_OPT_SET_EXACT_BYTES </p>
<p> Parameter<code>[1]</code>: Default flag for whether to exactly allocate memory<br />
 Type<code>[1]</code>: int </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This option will set the default flag for whether to exactly allocate memory when a Ustr needs to be resized. </p>
<p> <code>Note:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>For a single instance, the ustr_dupx_*()&nbsp;<wbr>functions can be used. </p>
<p> <code>Constant: </code> USTR_CNTL_OPT_GET_MEM<br />
 Parameter<code>[1]</code>: Pointer to colleciton of function pointers for system allocation<br />
 Type<code>[1]</code>: struct Ustr_cntl_mem * </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This option will get the&nbsp;<wbr>&quot;system&quot;&nbsp;<wbr>allocation functions&nbsp;<wbr>(malloc, realloc, free)&nbsp;<wbr>for allocated Ustr&#8217;s. </p>
<p> <code>Note:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>As you would expect the default values are: malloc, realloc, free. </p>
<p> <code>Constant: </code> USTR_CNTL_OPT_SET_MEM<br />
 Parameter<code>[1]</code>: Pointer to colleciton of function pointers for system allocation<br />
 Type<code>[1]</code>: const struct Ustr_cntl_mem * </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This option will set the&nbsp;<wbr>&quot;system&quot;&nbsp;<wbr>allocation functions&nbsp;<wbr>(malloc, realloc, free)&nbsp;<wbr>for allocated Ustr&#8217;s. </p>
<p> <code>Note:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>If this option is set after a Ustr has been created, then when freeing or reallocating the existing Ustr the given functions will be used. So they must either be compatible with the default or you must ensure that nothing is allocated before they are set. </p>
<p> <code>Constant: </code> USTR_CNTL_OPT_GET_MC_M_SCRUB </p>
<p> Parameter<code>[1]</code>: Flag for whether to include an explicit size in a Ustr<br />
 Type<code>[1]</code>: int * </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This option will get the flag for whether to&nbsp;<wbr>&quot;scrub&quot;&nbsp;<wbr>data allocated via. malloc check. </p>
<p> <code>Note:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Malloc check has to be enabled for this to mean anything, Ie. USTR_CNTL_MALLOC_LVL()&nbsp;<wbr>must be positive. </p>
<p> <code>Constant: </code> USTR_CNTL_OPT_SET_MC_M_SCRUB </p>
<p> Parameter<code>[1]</code>: Flag for whether to include an explicit size in a Ustr<br />
 Type<code>[1]</code>: int </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This option will set the flag for whether to&nbsp;<wbr>&quot;scrub&quot;&nbsp;<wbr>data allocated via. malloc check. </p>
<p> <code>Note:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Malloc check has to be enabled for this to mean anything, Ie. USTR_CNTL_MALLOC_LVL()&nbsp;<wbr>must be positive. </p>
<p> <code>Constant: </code> USTR_CNTL_OPT_GET_MC_F_SCRUB </p>
<p> Parameter<code>[1]</code>: Flag for whether to include an explicit size in a Ustr<br />
 Type<code>[1]</code>: int * </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This option will get the flag for whether to&nbsp;<wbr>&quot;scrub&quot;&nbsp;<wbr>data freed via. malloc check. </p>
<p> <code>Note:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Malloc check has to be enabled for this to mean anything, Ie. USTR_CNTL_MALLOC_LVL()&nbsp;<wbr>must be positive. </p>
<p> <code>Constant: </code> USTR_CNTL_OPT_SET_MC_F_SCRUB </p>
<p> Parameter<code>[1]</code>: Flag for whether to include an explicit size in a Ustr<br />
 Type<code>[1]</code>: int </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This option will set the flag for whether to&nbsp;<wbr>&quot;scrub&quot;&nbsp;<wbr>data freed via. malloc check. </p>
<p> <code>Note:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Malloc check has to be enabled for this to mean anything, Ie. USTR_CNTL_MALLOC_LVL()&nbsp;<wbr>must be positive. </p>
<p> <code>Constant: </code> USTR_CNTL_OPT_GET_MC_R_SCRUB </p>
<p> Parameter<code>[1]</code>: Flag for whether to include an explicit size in a Ustr<br />
 Type<code>[1]</code>: int * </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This option will get the flag for whether to&nbsp;<wbr>&quot;scrub&quot;&nbsp;<wbr>data reallocated via. malloc check. This is done by turning all reallocations into a malloc()&nbsp;<wbr>and free(), and so is even more costly than normal scrubbing. </p>
<p> <code>Note:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Malloc check has to be enabled for this to mean anything, Ie. USTR_CNTL_MALLOC_LVL()&nbsp;<wbr>must be positive. </p>
<p> <code>Constant: </code> USTR_CNTL_OPT_SET_MC_R_SCRUB </p>
<p> Parameter<code>[1]</code>: Flag for whether to include an explicit size in a Ustr<br />
 Type<code>[1]</code>: int </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This option will set the flag for whether to&nbsp;<wbr>&quot;scrub&quot;&nbsp;<wbr>data reallocated via. malloc check. This is done by turning all reallocations into a malloc()&nbsp;<wbr>and free(), and so is even more costly than normal scrubbing. </p>
<p> <code>Note:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Malloc check has to be enabled for this to mean anything, Ie. USTR_CNTL_MALLOC_LVL()&nbsp;<wbr>must be positive. </p>
<p> <code>Constant: </code> USTR_CNTL_OPT_GET_FMT<br />
 Parameter<code>[1]</code>: Pointer to colleciton of function pointers for system formating<br />
 Type<code>[1]</code>: struct Ustr_cntl_fmt * </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This option will get the system formatting functions&nbsp;<wbr>(vsnprintf)&nbsp;<wbr>for Ustr&#8217;s. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>There are two functions, the first is always called and the second is likely called&nbsp;<wbr>(always with the exact same arguments)&nbsp;<wbr>if the length passed to the first call was not big enough. </p>
<p> <code>Note:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>As you would expect the default values are: vsnprintf and vsnprintf </p>
<p> <code>Constant: </code> USTR_CNTL_OPT_SET_FMT<br />
 Parameter<code>[1]</code>: Pointer to colleciton of function pointers for system formatting<br />
 Type<code>[1]</code>: const struct Ustr_cntl_fmt * </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This option will set the system formatting functions&nbsp;<wbr>(vsnprintf)&nbsp;<wbr>for Ustr&#8217;s.</p>
<h2>Constants passed to ustr_pool_ll_cntl()</h2>
<p><code>Constant: </code> USTR_POOL_LL_CNTL_GET_FREE_CMP </p>
<p> Parameter<code>[1]</code>: Number of pointers to compare to in the pool<br />
 Type<code>[1]</code>: unsigned int * </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This option will get the number of comparisons done on a pool free operation. </p>
<p> <code>Constant: </code> USTR_POOL_LL_CNTL_SET_FREE_CMP </p>
<p> Parameter<code>[1]</code>: Number of pointers to compare to in the pool<br />
 Type<code>[1]</code>: unsigned int </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This option will set the number of comparisons done on a pool free operation. </p>
<p> <code>Note:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>The default is a small non-zero value, as it&#8217;s significantly common to have very short lived ustr&#8217;s &#8230; however this doesn&#8217;t mean that you can&#8217;t forget to take references even with pool allocated ustrs. </p>
<p> <code>Constant: </code> USTR_POOL_LL_CNTL_GET_REALLOC </p>
<p> Parameter<code>[1]</code>: Flag for if we should call realloc()<br />
 Type<code>[1]</code>: int * </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This option will get the flag for if we call realloc()&nbsp;<wbr>to make data bigger, or revert to just allocating anew each time. </p>
<p> <code>Constant: </code> USTR_POOL_LL_CNTL_SET_REALLOC </p>
<p> Parameter<code>[1]</code>: Flag for if we should call realloc()<br />
 Type<code>[1]</code>: int </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This option will set the flag for if we call realloc()&nbsp;<wbr>to make data bigger, or revert to just allocating anew each time. </p>
<p> <code>Note:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>As with USTR_POOL_LL_CNTL_SET_FREE_CMP this option means you can&#8217;t assume that pool allocated data is never freed until ustr_pool_free()&nbsp;<wbr>is called, and again it is due to there being significant speed improvements for not making that assumption. Instead of disabling this option, just take areference&nbsp;<wbr>(which will also make sure the ustr isn&#8217;t modified behind your back).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ustr/">ustr</a></code>(3) </p>
