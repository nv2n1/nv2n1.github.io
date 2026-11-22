---

title: "ustr(3)"
name: "ustr"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustr/"
description: "ustr – ustr string library functions"
---

<p> ustr - ustr string library functions  </p>

<p> #include &quot;ustr.h&quot; </p>
<p> <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>USTR</code>(void *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustrp *<code>USTRP</code>(void *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>USTR1</code>(symbol, const char[]); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>USTR2</code>(symbol, symbol, const char[]); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>USTR4</code>(symbol, symbol, symbol, symbol, const char[]); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>USTR1_CHK</code>(symbol, const char[]); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>USTR2_CHK</code>(symbol, symbol, const char[]); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>USTR4_CHK</code>(symbol, symbol, symbol, symbol, const char[]); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>USTRP1</code>(symbol, const char[]); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>USTRP2</code>(symbol, symbol, const char[]); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustrp *<code>USTRP4</code>(symbol, symbol, symbol, symbol, const char[]); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>USTRP1_CHK</code>(symbol, const char[]); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>USTRP2_CHK</code>(symbol, symbol, const char[]); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustrp *<code>USTRP4_CHK</code>(symbol, symbol, symbol, symbol, const char[]); </p>
<p> <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>USTR_SIZE_FIXED</code>(size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_init_fixed</code>(void *, size_t, int, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>USTR_SC_INIT_AUTO</code>(char[], int, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>USTR_SC_INIT_AUTO_OSTR</code>(char[], int, size_t); </p>
<p> <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_assert_valid</code>(Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_assert_valid_subustr</code>(Ustr *, size_t, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>USTR_CNTL_MALLOC_CHECK_BEG</code>(int); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>USTR_CNTL_MALLOC_CHECK_LVL</code>(void); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>USTR_CNTL_MALLOC_CHECK_MEM</code>(void *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>USTR_CNTL_MALLOC_CHECK_MEM_SZ</code>(void *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>USTR_CNTL_MALLOC_CHECK_MEM_MINSZ</code>(void *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>USTR_CNTL_MALLOC_CHECK_MEM_USTR</code>(Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>USTR_CNTL_MALLOC_CHECK_MEM_USTRP</code>(Ustrp *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>USTR_CNTL_MALLOC_CHECK_END</code>(void); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>USTR_CNTL_MALLOC_CHECK_ADD</code>(int); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>USTR_CNTL_MALLOC_CHECK_DEL</code>(int); </p>
<p> <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_init_size</code>(size_t, size_t, int, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_init_alloc</code>(void *, size_t, size_t, size_t, int, int, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_dupx_empty</code>(size_t, size_t, int, int); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_dup_empty</code>(void); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_dupx_undef</code>(size_t, size_t, int, int, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_dup_undef</code>(size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_dup</code>(const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_dupx</code>(size_t, size_t, int, int, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_sc_dup</code>(struct Ustr **); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_sc_dupx</code>(size_t, size_t, int, int, struct Ustr **); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_dup_buf</code>(const void *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_dupx_buf</code>(size_t, size_t, int, int, const void *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_dup_cstr</code>(const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_dupx_cstr</code>(size_t, size_t, int, int, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>USTR_DUP_OSTR</code>(const char []); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>USTR_DUP_OBJ</code>(...); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_dup_subustr</code>(const struct Ustr *, size_t, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_dupx_subustr</code>(size_t, size_t, int, int, const struct Ustr *, size_t, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_dup_rep_chr</code>(char, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_dupx_rep_chr</code>(size_t, size_t, int, int, char, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_sc_vjoin</code>(const struct Ustr *, const struct Ustr *, const struct Ustr *, va_list); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_sc_join</code>(const struct Ustr *, const struct Ustr *, const struct Ustr *, ...); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_sc_vjoinx</code>(size_t, size_t, int, int, const struct Ustr *, const struct Ustr *, const struct Ustr *, va_list); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_sc_joinx</code>(size_t, size_t, int, int, const struct Ustr *, const struct Ustr *, const struct Ustr *, ...); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_sc_vconcat</code>(const struct Ustr *, va_list); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_sc_concat</code>(const struct Ustr *, ...); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_sc_vconcatx</code>(size_t, size_t, int, int, const struct Ustr *, va_list); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_sc_concatx</code>(size_t, size_t, int, int, const struct Ustr *, ...); </p>
<p> <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> void <code>ustr_free</code>(struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> void <code>ustrp_free</code>(struct Ustr_pool *, struct Ustrp *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> void <code>ustr_sc_free</code>(struct Ustr **); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> void <code>ustr_sc_free2</code>(struct Ustr **, struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> void <code>ustr_sc_free_shared</code>(struct Ustr **); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_del</code>(struct Ustr **, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_del_subustr</code>(struct Ustr **, size_t, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> void <code>ustr_sc_del</code>(struct Ustr **); </p>
<p> <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_add_undef</code>(struct Ustr **, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_add_buf</code>(struct Ustr **, const void *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_add_cstr</code>(struct Ustr **, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>USTR_ADD_OSTR</code>(struct Ustr **, const char []); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>USTR_ADD_OBJ</code>(struct Ustr **, ...); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_add</code>(struct Ustr **, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_add_subustr</code>(struct Ustr **, const struct Ustr *, size_t, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_add_rep_chr</code>(struct Ustr **, char, size_t); </p>
<p> <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_set_undef</code>(struct Ustr **, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_set_empty</code>(struct Ustr **); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_set_buf</code>(struct Ustr **, const void *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_set_cstr</code>(struct Ustr **, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>USTR_SET_OSTR</code>(struct Ustr **, const char []); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>USTR_SET_OBJ</code>(struct Ustr **, ...); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_set</code>(struct Ustr **, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_set_subustr</code>(struct Ustr **, const struct Ustr *, size_t, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_set_rep_chr</code>(struct Ustr **, char, size_t); </p>
<p> <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_ins_undef</code>(struct Ustr **, size_t, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_ins_buf</code>(struct Ustr **, size_t, const void *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_ins_cstr</code>(struct Ustr **, size_t, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>USTR_INS_OSTR</code>(struct Ustr **, size_t, const char []); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>USTR_INS_OBJ</code>(struct Ustr **, size_t, ...); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_ins</code>(struct Ustr **, size_t, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_ins_subustr</code>(struct Ustr **, size_t, const struct Ustr *, size_t, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_ins_rep_chr</code>(struct Ustr **, size_t, char, size_t); </p>
<p> <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_add_vfmt_lim</code>(struct Ustr **, size_t, const char *, va_list); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_add_vfmt</code>(struct Ustr **, const char *, va_list); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_add_fmt_lim</code>(struct Ustr **, size_t, const char *, ...); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_add_fmt</code>(struct Ustr **, const char *, ...); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_dup_vfmt_lim</code>(size_t, const char *, va_list); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_dup_vfmt</code>(size_t, const char *, va_list); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_dup_fmt_lim</code>(size_t, const char *, ...); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_dup_fmt</code>(const char *, ...); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_dupx_fmt_lim</code>(size_t, size_t, int, int, size_t, const char *, ...); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_dupx_fmt</code>(size_t, size_t, int, int, const char *, ...); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_set_vfmt_lim</code>(struct Ustr **, size_t, const char *, va_list); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_set_vfmt</code>(struct Ustr **, const char *, va_list); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_set_fmt_lim</code>(struct Ustr **, size_t, const char *, ...); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_set_fmt</code>(struct Ustr **, const char *, ...); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_ins_vfmt_lim</code>(struct Ustr **, size_t, size_t, const char *, va_list); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_ins_vfmt</code>(struct Ustr **, size_t, const char *, va_list); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_ins_fmt_lim</code>(struct Ustr **, size_t, size_t, const char *, ...); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_ins_fmt</code>(struct Ustr **, size_t, const char *, ...); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sub_vfmt_lim</code>(struct Ustr **, size_t, size_t, const char *, va_list); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sub_vfmt</code>(struct Ustr **, size_t, const char *, va_list); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sub_fmt_lim</code>(struct Ustr **, size_t, size_t, const char *, ...); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sub_fmt</code>(struct Ustr **, size_t, const char *, ...); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sc_sub_vfmt_lim</code>(struct Ustr **, size_t, size_t, size_t, const char *, va_list); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sc_sub_vfmt</code>(struct Ustr **, size_t, size_t, const char *, va_list); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sc_sub_fmt_lim</code>(struct Ustr **, size_t, size_t, size_t, const char *, ...); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sc_sub_fmt</code>(struct Ustr **, size_t, size_t, const char *, ...); </p>
<p> <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_len</code>(const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> const char *<code>ustr_cstr</code>(const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> char *<code>ustr_wstr</code>(struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_alloc</code>(const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_exact</code>(const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sized</code>(const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_ro</code>(const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_fixed</code>(const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_enomem</code>(const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_shared</code>(const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_limited</code>(const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_owner</code>(const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_size</code>(const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_size_alloc</code>(const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_size_overhead</code>(const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> void <code>ustr_conf</code>(const struct Ustr *, size_t *, size_t *, int *, size_t *, size_t *); </p>
<p> <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_setf_enomem_err</code>(struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_setf_enomem_clr</code>(struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_setf_share</code>(struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_setf_owner</code>(struct Ustr *); </p>
<p> <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_buf</code>(const struct Ustr *, const void *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp</code>(const struct Ustr *, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_subustr</code>(const struct Ustr *, const struct Ustr *, size_t, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_cstr</code>(const struct Ustr *, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_fast_buf</code>(const struct Ustr *, const void *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_fast</code>(const struct Ustr *, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_fast_subustr</code>(const struct Ustr *, const struct Ustr *, size_t, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_fast_cstr</code>(const struct Ustr *, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_case_buf</code>(const struct Ustr *, const void *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_case</code>(const struct Ustr *, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_case_subustr</code>(const struct Ustr *, const struct Ustr *, size_t, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_case_cstr</code>(const struct Ustr *, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_eq</code>(const struct Ustr *, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_buf_eq</code>(const struct Ustr *, const void *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_subustr_eq</code>(const struct Ustr *, const struct Ustr *, size_t, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_cstr_eq</code>(const struct Ustr *, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_case_eq</code>(const struct Ustr *, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_case_buf_eq</code>(const struct Ustr *, const void *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_case_subustr_eq</code>(const struct Ustr *, const struct Ustr *, size_t, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_case_cstr_eq</code>(const struct Ustr *, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_prefix_eq</code>(const struct Ustr *, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_prefix_buf_eq</code>(const struct Ustr *, const void *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_prefix_cstr_eq</code>(const struct Ustr *, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_prefix_subustr_eq</code>(const struct Ustr *, const struct Ustr *, size_t, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_case_prefix_eq</code>(const struct Ustr *, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_case_prefix_buf_eq</code>(const struct Ustr *, const void *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_case_prefix_cstr_eq</code>(const struct Ustr *, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_case_prefix_subustr_eq</code>(const struct Ustr *, const struct Ustr *, size_t, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_suffix_eq</code>(const struct Ustr *, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_suffix_buf_eq</code>(const struct Ustr *, const void *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_suffix_cstr_eq</code>(const struct Ustr *, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_suffix_subustr_eq</code>(const struct Ustr *, const struct Ustr *, size_t, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_case_suffix_eq</code>(const struct Ustr *, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_case_suffix_buf_eq</code>(const struct Ustr *, const void *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_case_suffix_cstr_eq</code>(const struct Ustr *, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cmp_case_suffix_subustr_eq</code>(const struct Ustr *, const struct Ustr *, size_t, size_t); </p>
<p> <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_srch_chr_fwd</code>(const struct Ustr *, size_t, char); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_srch_chr_rev</code>(const struct Ustr *, size_t, char); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_srch_buf_fwd</code>(const struct Ustr *, size_t, const void *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_srch_buf_rev</code>(const struct Ustr *, size_t, const void *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_srch_fwd</code>(const struct Ustr *, size_t, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_srch_rev</code>(const struct Ustr *, size_t, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_srch_cstr_fwd</code>(const struct Ustr *, size_t, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_srch_cstr_rev</code>(const struct Ustr *, size_t, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_srch_subustr_fwd</code>(const struct Ustr *, size_t, const struct Ustr *, size_t, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_srch_subustr_rev</code>(const struct Ustr *, size_t, const struct Ustr *, size_t, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_srch_case_chr_fwd</code>(const struct Ustr *, size_t, char); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_srch_case_chr_rev</code>(const struct Ustr *, size_t, char); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_srch_case_buf_fwd</code>(const struct Ustr *, size_t, const void *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_srch_case_buf_rev</code>(const struct Ustr *, size_t, const void *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_srch_case_fwd</code>(const struct Ustr *, size_t, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_srch_case_rev</code>(const struct Ustr *, size_t, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_srch_case_cstr_fwd</code>(const struct Ustr *, size_t, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_srch_case_cstr_rev</code>(const struct Ustr *, size_t, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_srch_case_subustr_fwd</code>(const struct Ustr *, size_t, const struct Ustr *, size_t, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_srch_case_subustr_rev</code>(const struct Ustr *, size_t, const struct Ustr *, size_t, size_t); </p>
<p> <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_spn_chr_fwd</code>(const struct Ustr *, size_t, char); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_spn_chr_rev</code>(const struct Ustr *, size_t, char); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_spn_chrs_fwd</code>(const struct Ustr *, size_t, const char *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_spn_chrs_rev</code>(const struct Ustr *, size_t, const char *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_spn_fwd</code>(const struct Ustr *, size_t, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_spn_rev</code>(const struct Ustr *, size_t, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_spn_cstr_fwd</code>(const struct Ustr *, size_t, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_spn_cstr_rev</code>(const struct Ustr *, size_t, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_cspn_chr_fwd</code>(const struct Ustr *, size_t, char); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_cspn_chr_rev</code>(const struct Ustr *, size_t, char); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_cspn_chrs_fwd</code>(const struct Ustr *, size_t, const char *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_cspn_chrs_rev</code>(const struct Ustr *, size_t, const char *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_cspn_fwd</code>(const struct Ustr *, size_t, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_cspn_rev</code>(const struct Ustr *, size_t, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_cspn_cstr_fwd</code>(const struct Ustr *, size_t, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_cspn_cstr_rev</code>(const struct Ustr *, size_t, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_utf8_spn_chrs_fwd</code>(const struct Ustr *, size_t, const char *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_utf8_spn_chrs_rev</code>(const struct Ustr *, size_t, const char *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_utf8_spn_fwd</code>(const struct Ustr *, size_t, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_utf8_spn_rev</code>(const struct Ustr *, size_t, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_utf8_spn_cstr_fwd</code>(const struct Ustr *, size_t, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_utf8_spn_cstr_rev</code>(const struct Ustr *, size_t, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_utf8_cspn_chrs_fwd</code>(const struct Ustr *, size_t, const char *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_utf8_cspn_chrs_rev</code>(const struct Ustr *, size_t, const char *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_utf8_cspn_fwd</code>(const struct Ustr *, size_t, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_utf8_cspn_rev</code>(const struct Ustr *, size_t, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_utf8_cspn_cstr_fwd</code>(const struct Ustr *, size_t, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_utf8_cspn_cstr_rev</code>(const struct Ustr *, size_t, const char *); </p>
<p> <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_io_get</code>(struct Ustr **, FILE *, size_t, size_t *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_io_getfile</code>(struct Ustr **, FILE *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_io_getfilename</code>(struct Ustr **, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_io_getdelim</code>(struct Ustr **, FILE *, char); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_io_getline</code>(struct Ustr **, FILE *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_io_put</code>(struct Ustr **, FILE *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_io_putline</code>(struct Ustr **, FILE *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_io_putfile</code>(struct Ustr **, FILE *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_io_putfileline</code>(struct Ustr **, FILE *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_io_putfilename</code>(struct Ustr **, const char *, const char *); </p>
<p> <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sub_undef</code>(struct Ustr **, size_t, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sub_buf</code>(struct Ustr **, size_t, const void *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sub_cstr</code>(struct Ustr **, size_t, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>USTR_SUB_OSTR</code>(struct Ustr **, size_t, const char []); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>USTR_SUB_OBJ</code>(struct Ustr **, size_t, ...); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sub</code>(struct Ustr **, size_t, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sub_subustr</code>(struct Ustr **, size_t, const struct Ustr *, size_t, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sc_sub_undef</code>(struct Ustr **, size_t, size_t, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sc_sub_buf</code>(struct Ustr **, size_t , size_t , const void *, size_t ); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sc_sub_cstr</code>(struct Ustr **, size_t, size_t, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sc_sub</code>(struct Ustr **, size_t, size_t, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sc_sub_subustr</code>(struct Ustr **, size_t, size_t, const struct Ustr *, size_t, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>USTR_SC_SUB_OSTR</code>(struct Ustr **, size_t, size_t, const char []); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>USTR_SC_SUB_OBJ</code>(struct Ustr **, size_t, size_t, ...); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_replace_buf</code>(struct Ustr **, const void *, size_t, const void *, size_t, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_replace_cstr</code>(struct Ustr **, const char *, const char *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_replace</code>(struct Ustr **, const struct Ustr *, const struct Ustr *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_replace_rep_chr</code>(struct Ustr **ps1, char, size_t, char, size_t nlen, size_t lim); </p>
<p> <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_split_buf</code>(const struct Ustr *, size_t *, const void *, size_t, struct Ustr *, unsigned int); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_split</code>(const struct Ustr *, size_t *, const struct Ustr *, struct Ustr *, unsigned int); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_split_cstr</code>(const struct Ustr *, size_t *, const char *, struct Ustr *, unsigned int); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_split_spn_chrs</code>(const struct Ustr *, size_t *, const char *, size_t, struct Ustr *, unsigned int); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_split_spn_cstr</code>(const struct Ustr *, size_t *, const char *, struct Ustr *, unsigned int); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr *<code>ustr_split_spn</code>(const struct Ustr *, size_t *, const struct Ustr *, struct Ustr *, unsigned int); </p>
<p> <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_utf8_valid</code>(const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_utf8_len</code>(const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> ssize_t <code>ustr_utf8_width</code>(const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_utf8_chars2bytes</code>(const struct Ustr *, size_t, size_t, size_t *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> size_t <code>ustr_utf8_bytes2chars</code>(const struct Ustr *, size_t, size_t, size_t *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sc_utf8_reverse</code>(struct Ustr **); </p>
<p> <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> uintmax_t <code>ustr_parse_uintmaxx</code>(const struct Ustr *, size_t, unsigned int, uintmax_t, uintmax_t, const char *, size_t *, unsigned int *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> uintmax_t <code>ustr_parse_uintmax</code>(const struct Ustr *, size_t, unsigned int, size_t *, unsigned int *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> intmax_t <code>ustr_parse_intmax</code>(const struct Ustr *, size_t, unsigned int, size_t *, unsigned int *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> unsigned long <code>ustr_parse_ulongx</code>(const struct Ustr *, size_t, unsigned int, unsigned long, unsigned long, const char *, size_t *, unsigned int *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> unsigned long <code>ustr_parse_ulong</code>(const struct Ustr *, size_t, unsigned int, size_t *, unsigned int *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> long <code>ustr_parse_long</code>(const struct Ustr *, size_t, unsigned int, size_t *, unsigned int *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> unsigned int <code>ustr_parse_uint</code>(const struct Ustr *, size_t, unsigned int, size_t *, unsigned int *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_parse_int</code>(const struct Ustr *, size_t, unsigned int, size_t *, unsigned int *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> unsigned short <code>ustr_parse_ushort</code>(const struct Ustr *, size_t, unsigned int, size_t *, unsigned int *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> short <code>ustr_parse_short</code>(const struct Ustr *, size_t, unsigned int, size_t *, unsigned int *); </p>
<p> <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sc_ensure_owner</code>(struct Ustr **); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> char *<code>ustr_sc_wstr</code>(struct Ustr **); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> char *<code>ustr_sc_export_subustr</code>(const struct Ustr *, size_t, size_t, void *(*)(size_t)); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> char *<code>ustr_sc_export</code>(const struct Ustr *, void *(*)(size_t)); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> char *<code>ustrp_sc_export_subustrp</code>(struct Ustr_pool *, const struct Ustr *, size_t, size_t, void *(*)(size_t)); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> char *<code>ustrp_sc_export</code>(struct Ustr_pool *, const struct Ustr *, void *(*)(size_t)); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sc_reverse</code>(struct Ustr **); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sc_tolower</code>(struct Ustr **); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sc_toupper</code>(struct Ustr **); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sc_ltrim_chrs</code>(struct Ustr **, const char *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sc_ltrim</code>(struct Ustr **, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sc_ltrim_cstr</code>(struct Ustr **, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sc_rtrim_chrs</code>(struct Ustr **, const char *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sc_rtrim</code>(struct Ustr **, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sc_rtrim_cstr</code>(struct Ustr **, const char *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sc_trim_chrs</code>(struct Ustr **, const char *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sc_trim</code>(struct Ustr **, const struct Ustr *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_sc_trim_cstr</code>(struct Ustr **, const char *); </p>
<p> <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_add_b_uint16</code>(struct Ustr **, uint_least16_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_add_b_uint32</code>(struct Ustr **, uint_least32_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_add_b_uint64</code>(struct Ustr **, uint_least64_t); </p>
<p> <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> uint_least16_t <code>ustr_parse_b_uint16</code>(const struct Ustr *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> uint_least32_t <code>ustr_parse_b_uint32</code>(const struct Ustr *, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> uint_least64_t <code>ustr_parse_b_uint64</code>(const struct Ustr *, size_t); </p>
<p> <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_realloc</code>(struct Ustr **, size_t); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> int <code>ustr_cntl_opt</code>(int, ...); </p>
<p> <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr_pool *<code>ustr_pool_ll_make</code>(void); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> struct Ustr_pool *<code>ustr_pool_make_subpool</code>(struct Ustr_pool *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> void <code>ustr_pool_free</code>(struct Ustr_pool *); <br/>
 <br/>
 &nbsp;<wbr>&nbsp;<wbr> void <code>ustr_pool_clear</code>(struct Ustr_pool *); </p>
<p> <br/>
 create constant/read-only strings, and USTR_SC_INIT_AUTO() to create strings that use stack space upto a certain amount. <br/>
&nbsp;<wbr>Use is somewhat unique in that, by default, it has an average overhead of only 55% overhead over strdup(), for strings in the range of 0 to 20 bytes. Or, to put it another way it only uses 8 bytes to store a 2 byte string where strdup() uses 3.  </p>
<h2>Creating read-only Ustr functions</h2>
<p> <br/>
 <br/>
 <code>Function: </code> USTR() <br/>
 Returns: Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to Ustr data <br/>
 Type <code>[1]</code>: void * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This macro function is normally used with the empty string&nbsp;<wbr>&quot;&quot;. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>There is basically just a simple cast behind the macro. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTRP() <br/>
 Returns: Ustrp string <br/>
 Type: struct Ustrp * </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to Ustrp data <br/>
 Type <code>[1]</code>: void * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This macro function is normally used with the empty string&nbsp;<wbr>&quot;&quot;. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>There is basically just a simple cast behind the macro. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR1() <br/>
 Returns: Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Encoded number of the length of Ustr string <br/>
 Type <code>[1]</code>: symbol </p>
<p> <br/>
 Parameter <code>[2]</code>: Data for Ustr string <br/>
 Type <code>[2]</code>: const char[] </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This macro function simplifies the creation of read-only Ustr string&#8217;s. And is normally used like... </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>USTR1(\x4,&nbsp;<wbr>&quot;abcd&quot;) </p>
<p> <br/>
&nbsp;<wbr>...it is worth pointing out that running with debugging turned on <br/>
&nbsp;<wbr>(USTR_CONF_USE_ASSERT)&nbsp;<wbr>will complain if the length isn&#8217;t encoded correctly, as in... </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>USTR1(\x3,&nbsp;<wbr>&quot;abcd&quot;) </p>
<p> <br/>
&nbsp;<wbr>...here ustr_assert_valid()&nbsp;<wbr>will fail, which is called before most functions do <br/>
&nbsp;<wbr>anything in debugging mode. Note also that extra debugging&nbsp;<wbr>(USTR_CONF_USE_EOS_MARK)&nbsp;<wbr>will still catch cases like... </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>USTR1(\x3,&nbsp;<wbr>&quot;abc\0d&quot;) </p>
<p> <br/>
&nbsp;<wbr>...at least using debugging is esp. important if you are putting UTF-8 <br/>
&nbsp;<wbr>characters into the strings. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>Having ustr_ro()&nbsp;<wbr>return true means that the Ustr cannot be written to without be reallocated into allocation space ... not that ustr_add()&nbsp;<wbr>etc. will fail. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>There is now USTR1_CHK()&nbsp;<wbr>which performs a compile time check so you can never have an invalid ustr. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR2() <br/>
 Returns: Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Encoded 2nd byte of number of the length of Ustr string <br/>
 Type <code>[1]</code>: symbol </p>
<p> <br/>
 Parameter <code>[2]</code>: Encoded 1st byte of number of the length of Ustr string <br/>
 Type <code>[2]</code>: symbol </p>
<p> <br/>
 Parameter <code>[3]</code>: Data for Ustr string <br/>
 Type <code>[3]</code>: const char[] </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works in the same way as USTR1()&nbsp;<wbr>but takes two length bytes, so the read-only string can be upto 65,535&nbsp;<wbr>(2**16 - 1)&nbsp;<wbr>bytes in length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR4() <br/>
 Returns: Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Encoded 4th byte of number of the length of Ustr string <br/>
 Type <code>[1]</code>: symbol </p>
<p> <br/>
 Parameter <code>[2]</code>: Encoded 3rd byte of number of the length of Ustr string <br/>
 Type <code>[2]</code>: symbol </p>
<p> <br/>
 Parameter <code>[3]</code>: Encoded 2nd byte of number of the length of Ustr string <br/>
 Type <code>[3]</code>: symbol </p>
<p> <br/>
 Parameter <code>[4]</code>: Encoded 1st byte of number of the length of Ustr string <br/>
 Type <code>[4]</code>: symbol </p>
<p> <br/>
 Parameter <code>[5]</code>: Data for Ustr string <br/>
 Type <code>[5]</code>: const char[] </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works in the same way as USTR1()&nbsp;<wbr>but takes four length bytes, so the read-only string can be upto 2**32 - 1 bytes in length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR1_CHK() <br/>
 Returns: Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Encoded number of the length of Ustr string <br/>
 Type <code>[1]</code>: symbol </p>
<p> <br/>
 Parameter <code>[2]</code>: Data for Ustr string <br/>
 Type <code>[2]</code>: const char[] </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works in the same way as USTR1()&nbsp;<wbr>but it does a check against the length of&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>using sizeof()&nbsp;<wbr>- 1. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>If the check fails the returned Ustr&nbsp;<wbr>*&nbsp;<wbr>will be&nbsp;<wbr>&quot;&quot;, so you can check ustr_len()&nbsp;<wbr>to see if you screwed something up. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR2_CHK() <br/>
 Returns: Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Encoded 2nd byte of number of the length of Ustr string <br/>
 Type <code>[1]</code>: symbol </p>
<p> <br/>
 Parameter <code>[2]</code>: Encoded 1st byte of number of the length of Ustr string <br/>
 Type <code>[2]</code>: symbol </p>
<p> <br/>
 Parameter <code>[3]</code>: Data for Ustr string <br/>
 Type <code>[3]</code>: const char[] </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works in the same way as USTR2()&nbsp;<wbr>but it does a check against the length of&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>using sizeof()&nbsp;<wbr>- 1. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>If the check fails the returned Ustr&nbsp;<wbr>*&nbsp;<wbr>will be&nbsp;<wbr>&quot;&quot;. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR4_CHK() <br/>
 Returns: Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Encoded 4th byte of number of the length of Ustr string <br/>
 Type <code>[1]</code>: symbol </p>
<p> <br/>
 Parameter <code>[2]</code>: Encoded 3rd byte of number of the length of Ustr string <br/>
 Type <code>[2]</code>: symbol </p>
<p> <br/>
 Parameter <code>[3]</code>: Encoded 2nd byte of number of the length of Ustr string <br/>
 Type <code>[3]</code>: symbol </p>
<p> <br/>
 Parameter <code>[4]</code>: Encoded 1st byte of number of the length of Ustr string <br/>
 Type <code>[4]</code>: symbol </p>
<p> <br/>
 Parameter <code>[5]</code>: Data for Ustr string <br/>
 Type <code>[5]</code>: const char[] </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works in the same way as USTR4()&nbsp;<wbr>but it does a check against the length of&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>using sizeof()&nbsp;<wbr>- 1. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>If the check fails the returned Ustr&nbsp;<wbr>*&nbsp;<wbr>will be&nbsp;<wbr>&quot;&quot;. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTRP1() <br/>
 Returns: Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Encoded number of the length of Ustr string <br/>
 Type <code>[1]</code>: symbol </p>
<p> <br/>
 Parameter <code>[2]</code>: Data for Ustr string <br/>
 Type <code>[2]</code>: const char[] </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like USTR1(), but returns a Ustrp instead. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTRP2() <br/>
 Returns: Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Encoded 2nd byte of number of the length of Ustr string <br/>
 Type <code>[1]</code>: symbol </p>
<p> <br/>
 Parameter <code>[2]</code>: Encoded 1st byte of number of the length of Ustr string <br/>
 Type <code>[2]</code>: symbol </p>
<p> <br/>
 Parameter <code>[3]</code>: Data for Ustr string <br/>
 Type <code>[3]</code>: const char[] </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like USTR4(), but returns a Ustrp instead. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTRP4() <br/>
 Returns: Ustrp string <br/>
 Type: struct Ustrp * </p>
<p> <br/>
 Parameter <code>[1]</code>: Encoded 4th byte of number of the length of Ustrp string <br/>
 Type <code>[1]</code>: symbol </p>
<p> <br/>
 Parameter <code>[2]</code>: Encoded 3rd byte of number of the length of Ustrp string <br/>
 Type <code>[2]</code>: symbol </p>
<p> <br/>
 Parameter <code>[3]</code>: Encoded 2nd byte of number of the length of Ustrp string <br/>
 Type <code>[3]</code>: symbol </p>
<p> <br/>
 Parameter <code>[4]</code>: Encoded 1st byte of number of the length of Ustrp string <br/>
 Type <code>[4]</code>: symbol </p>
<p> <br/>
 Parameter <code>[5]</code>: Data for Ustr string <br/>
 Type <code>[5]</code>: const char[] </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like USTR2(), but returns a Ustrp instead. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTRP1_CHK() <br/>
 Returns: Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Encoded number of the length of Ustr string <br/>
 Type <code>[1]</code>: symbol </p>
<p> <br/>
 Parameter <code>[2]</code>: Data for Ustr string <br/>
 Type <code>[2]</code>: const char[] </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like USTR1_CHK(), but returns a Ustrp instead. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTRP2_CHK() <br/>
 Returns: Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Encoded 2nd byte of number of the length of Ustr string <br/>
 Type <code>[1]</code>: symbol </p>
<p> <br/>
 Parameter <code>[2]</code>: Encoded 1st byte of number of the length of Ustr string <br/>
 Type <code>[2]</code>: symbol </p>
<p> <br/>
 Parameter <code>[3]</code>: Data for Ustr string <br/>
 Type <code>[3]</code>: const char[] </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like USTR4_CHK(), but returns a Ustrp instead. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTRP4_CHK() <br/>
 Returns: Ustrp string <br/>
 Type: struct Ustrp * </p>
<p> <br/>
 Parameter <code>[1]</code>: Encoded 4th byte of number of the length of Ustrp string <br/>
 Type <code>[1]</code>: symbol </p>
<p> <br/>
 Parameter <code>[2]</code>: Encoded 3rd byte of number of the length of Ustrp string <br/>
 Type <code>[2]</code>: symbol </p>
<p> <br/>
 Parameter <code>[3]</code>: Encoded 2nd byte of number of the length of Ustrp string <br/>
 Type <code>[3]</code>: symbol </p>
<p> <br/>
 Parameter <code>[4]</code>: Encoded 1st byte of number of the length of Ustrp string <br/>
 Type <code>[4]</code>: symbol </p>
<p> <br/>
 Parameter <code>[5]</code>: Data for Ustr string <br/>
 Type <code>[5]</code>: const char[] </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like USTR2_CHK(), but returns a Ustrp instead. </p>
<h2>Creating fixed Ustr functions</h2>
<p> <br/>
 <br/>
 <code>Function: </code> USTR_SIZE_FIXED() <br/>
 Returns: Size of area of memory <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: Size of area of memory <br/>
 Type <code>[1]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This macro function is replaced by a static conversion from the max length desired&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>to the storage size needed. In other words it works out what ustr_size_overhead()&nbsp;<wbr>will be, and adds that value. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This is useful is you want a small fixed size allocation, as you can declare it like so: </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>char buf[USTR_SIZE_FIXED(4)]; <br/>
&nbsp;<wbr>...to give you exactly 4 bytes as a maximum, this is esp. useful if you want <br/>
&nbsp;<wbr>a limited&nbsp;<wbr>(ustr_limited()&nbsp;<wbr>==&nbsp;<wbr>USTR_TRUE)&nbsp;<wbr>Ustr string. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_init_fixed() <br/>
 Returns: Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to area of memory to use as a Ustr string <br/>
 Type <code>[1]</code>: void * </p>
<p> <br/>
 Parameter <code>[2]</code>: Size of area of memory <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Whether the fixed size Ustr should be limited <br/>
 Type <code>[3]</code>: int </p>
<p> <br/>
 Parameter <code>[4]</code>: The initial length of the Ustr <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This creates a new Ustr string, which is&nbsp;<wbr>&quot;fixed&quot;. This means the Ustr storage is managed outside of the ustr_*&nbsp;<wbr>API, it is often used for stack allocated strings. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>As you add data to the Ustr past the size allowed via. the fixed storge the Ustr will automatically be converted into an allocated Ustr. So if this is possible you should always call ustr_free(), as this does nothing if given a fixed size Ustr. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>For simplicity you probably want to use USTR_SC_INIT_AUTO()&nbsp;<wbr>or USTR_SC_INIT_AUTO()&nbsp;<wbr>when possible. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR_SC_INIT_AUTO() <br/>
 Returns: Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Area of memory to use as a Ustr string <br/>
 Type <code>[1]</code>: char[] </p>
<p> <br/>
 Parameter <code>[2]</code>: Whether the fixed size Ustr should be limited <br/>
 Type <code>[2]</code>: int </p>
<p> <br/>
 Parameter <code>[3]</code>: The initial length of the Ustr <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This calls ustr_init_fixed()&nbsp;<wbr>with sizeof()&nbsp;<wbr>the area of memory&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>as the second argument. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This does mean that the first argument must be the correct size, as far as sizeof()&nbsp;<wbr>is concerned, as in... </p>
<p> <br/>
&nbsp;<wbr>char buf_sz[1024]; <br/>
&nbsp;<wbr>Ustr&nbsp;<wbr>*s1&nbsp;<wbr>=&nbsp;<wbr>USTR_SC_INIT_AUTO(buf_sz, USTR_FALSE, 0); </p>
<p> <br/>
&nbsp;<wbr>...so passing pointers to memory from malloc()&nbsp;<wbr>will probably just return NULL. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR_SC_INIT_AUTO_OSTR() <br/>
 Returns: Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Area of memory to use as a Ustr string <br/>
 Type <code>[1]</code>: char[] </p>
<p> <br/>
 Parameter <code>[2]</code>: Whether the fixed size Ustr should be limited <br/>
 Type <code>[2]</code>: int </p>
<p> <br/>
 Parameter <code>[3]</code>: The initial string in the buffer, as a constant string <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This calls ustr_init_fixed()&nbsp;<wbr>with sizeof()&nbsp;<wbr>the area of memory&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>as the second argument, given as an&nbsp;<wbr>&quot;object string&quot;. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This does mean that the first argument must be the correct size, as far as sizeof()&nbsp;<wbr>is concerned, as in... </p>
<p> <br/>
&nbsp;<wbr>char buf_sz[1024]&nbsp;<wbr>=&nbsp;<wbr>USTR_BEG_FIXED2&nbsp;<wbr>&quot;abcd&quot;; <br/>
&nbsp;<wbr>Ustr&nbsp;<wbr>*s1&nbsp;<wbr>=&nbsp;<wbr>USTR_SC_INIT_AUTO_OSTR(buf_sz, USTR_FALSE,&nbsp;<wbr>&quot;abcd&quot;); </p>
<p> <br/>
&nbsp;<wbr>...so passing pointers to memory from malloc()&nbsp;<wbr>will probably just return NULL. </p>
<h2>Debugging functions</h2>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_assert_valid() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a Ustr string <br/>
 Type <code>[1]</code>: Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function asserts a few internal consistency checks, and can help point out when a Ustr is invalid. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This calls ustr_assert_ret()&nbsp;<wbr>so that when USTR_DEBUG if off the checks are still performed and the result is returned. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_assert_valid_subustr() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a Ustr string <br/>
 Type <code>[1]</code>: Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Position in the Ustr <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Length to delete from the Ustr <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function calls ustr_assert_valid()&nbsp;<wbr>and also checks that the position and length are within the Ustr. If they aren&#8217;t valid it returns 0, if they are valid it returns ustr_len(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR_CNTL_MALLOC_CHECK_BEG() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Condition for begin malloc checking or not <br/>
 Type <code>[1]</code>: int </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function begins malloc checking, meaning all ustr allocations will go through the malloc check routines, but it fails if the condition check&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>fails. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>Turning malloc checking on after one or more allocations has happened will lead to false failures unless you really known what you are doing. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>You can automatically turn malloc checking on by giving the USTR_CNTL_MC environment variable the value of&nbsp;<wbr>&quot;1&quot;,&nbsp;<wbr>&quot;yes&quot;&nbsp;<wbr>or&nbsp;<wbr>&quot;on&quot;. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR_CNTL_MALLOC_CHECK_LVL() <br/>
 Returns: Level of current malloc check <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Nothing <br/>
 Type <code>[1]</code>: void </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function returns the current&nbsp;<wbr>&quot;level&quot;&nbsp;<wbr>of the malloc check, with 0 indicating that malloc check isn&#8217;t enabled. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>The level goes up by one whenever USTR_CNTL_MALLOC_CHECK_BEG()&nbsp;<wbr>or USTR_CNTL_MALLOC_CHECK_ADD()&nbsp;<wbr>returns success, and goes down by one whenever USTR_CNTL_MALLOC_CHECK_DEL()&nbsp;<wbr>or USTR_CNTL_MALLOC_CHECK_END()&nbsp;<wbr>returns success. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR_CNTL_MALLOC_CHECK_MEM() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer returned from malloc check <br/>
 Type <code>[1]</code>: void * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function asserts that the pointer&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>was allocated from malloc checking. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>Unless you are doing something special, or using a builtin Ustr_pool it is very likely you want to just call USTR_CNTL_MALLOC_CHECK_MEM_USTR(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR_CNTL_MALLOC_CHECK_MEM_SZ() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer returned from malloc check <br/>
 Type <code>[1]</code>: void * </p>
<p> <br/>
 Parameter <code>[2]</code>: Length of allocated memory <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function asserts that the pointer&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>was allocated from malloc checking, and has the specified size&nbsp;<wbr>(Parameter[2]). </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>Unless you are doing something special, or using a builtin Ustr_pool it is very likely you want to just call USTR_CNTL_MALLOC_CHECK_MEM_USTR(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR_CNTL_MALLOC_CHECK_MEM_MINSZ() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer returned from malloc check <br/>
 Type <code>[1]</code>: void * </p>
<p> <br/>
 Parameter <code>[2]</code>: Length of allocated memory <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function asserts that the pointer&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>was allocated from malloc checking, and has at least the specified size&nbsp;<wbr>(Parameter[2]). </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>Unless you are doing something special, or using a builtin Ustr_pool it is very likely you want to just call USTR_CNTL_MALLOC_CHECK_MEM_USTR(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR_CNTL_MALLOC_CHECK_MEM_USTR() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a Ustr string <br/>
 Type <code>[1]</code>: Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function asserts that the pointer&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>is a Ustr allocated from malloc checking, if the Ustr is allocated&nbsp;<wbr>(if not it returns TRUE). </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>Because of the layering between the Ustr code and the pool code, if you allocate an implicity sized Ustrp from a pool and then delete some data from it&nbsp;<wbr>(which fails)&nbsp;<wbr>the Ustr layer will think it has an implicit less than the actual size so this function will fail. This is what USTR_CNTL_MALLOC_CHECK_MEM_USTRP()&nbsp;<wbr>is for. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR_CNTL_MALLOC_CHECK_MEM_USTRP() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a Ustrp string <br/>
 Type <code>[1]</code>: Ustrp * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function asserts that the pointer&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>is a Ustr allocated from a builtin pool using malloc checking, if the Ustr is allocated&nbsp;<wbr>(if not it returns TRUE). </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR_CNTL_MALLOC_CHECK_END() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Nothing <br/>
 Type <code>[1]</code>: void </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This macro will cleanup any memory used by malloc check, and assert that no memory is left allocated. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>If any memory is left allocated, each one found is output to stderr with the file/line/function of the level it was allocated from. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR_CNTL_MALLOC_CHECK_ADD() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Condition to begin malloc checking or not <br/>
 Type <code>[1]</code>: int </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like USTR_CNTL_MALLOC_CHECK_END()&nbsp;<wbr>but it fails if the condition check&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>fails, or if USTR_CNTL_MALLOC_CHECK_LVL()&nbsp;<wbr>is zero. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR_CNTL_MALLOC_CHECK_DEL() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Condition to end malloc checking or not <br/>
 Type <code>[1]</code>: int </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like USTR_CNTL_MALLOC_CHECK_END()&nbsp;<wbr>but it fails if the condition check&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>fails, or if USTR_CNTL_MALLOC_CHECK_LVL()&nbsp;<wbr>is one. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>The condition&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>to this macro should almost certainly be the return value from USTR_CNTL_MALLOC_CHECK_ADD(). </p>
<h2>Creating allocated Ustr functions</h2>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_init_size() <br/>
 Returns: Size that needs to be allocated <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: Size of allocated storage <br/>
 Type <code>[1]</code>: size_t </p>
<p> <br/>
 Parameter <code>[2]</code>: Number of bytes to use for reference count <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Exact memory allocations <br/>
 Type <code>[3]</code>: int </p>
<p> <br/>
 Parameter <code>[4]</code>: Length of data in the Ustr <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function finds out the exact size of memory needed to store the specified Ustr of the given configuration. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_init_alloc() <br/>
 Returns: Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to area of memory to use as a Ustr string <br/>
 Type <code>[1]</code>: void * </p>
<p> <br/>
 Parameter <code>[2]</code>: Size of area of memory <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Whether Ustr should store the size <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: Number of bytes to use for references <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 Parameter <code>[5]</code>: Whether the Ustr should use exact allocations <br/>
 Type <code>[5]</code>: int </p>
<p> <br/>
 Parameter <code>[6]</code>: Whether the Ustr should have the &quot;enomem&quot; flag set <br/>
 Type <code>[6]</code>: int </p>
<p> <br/>
 Parameter <code>[7]</code>: The initial length of the Ustr <br/>
 Type <code>[7]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This creates a new Ustr string, you should have allocated the data via.&nbsp;<wbr>&nbsp;<wbr>USTR_CONF_MALLOC()&nbsp;<wbr>or bad things will happen if the Ustr string is ever free&#8217;d or reallocated. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_dupx_empty() <br/>
 Returns: Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Size of allocated storage <br/>
 Type <code>[1]</code>: size_t </p>
<p> <br/>
 Parameter <code>[2]</code>: Number of bytes to use for reference count <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Exact memory allocation flag <br/>
 Type <code>[3]</code>: int </p>
<p> <br/>
 Parameter <code>[4]</code>: ENOMEM, memory error flag <br/>
 Type <code>[4]</code>: int </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function creates an empty Ustr, owned by you, that is allocated from system memory, or it returns NULL. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>The size is the desired allocation size for the entire Ustr, including overhead for metadata. This value will be rounded up, if it&#8217;s too small, so passing 1 as the size means you want a stored size but to allocate the smallest amount of memory possible. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>The exact memory allocation flag says if the Ustr should round allocations up to the nearest half power of two or should be no more than needed. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>The ENOMEM memory error flag sets the iniital state of the user visible flag for memory allocation errors. Eg. ustr_enomem(), ustr_setf_enomem_clr()&nbsp;<wbr>and ustr_setf_enomem_err() </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>The reference byte count can only be one of the following values: 0, 1, 2 or 4, or 8&nbsp;<wbr>(on environments with a 64bit size_t). <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>It can be useful to ensure that the Ustr is in system memory, so that you can add things to it and check for errors with ustr_enomem(). <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>If you chose to store the allocated size in the Ustr then the number of bytes allocated for the reference count will be a minimum of 2. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_dup_empty() <br/>
 Returns: Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Nothing <br/>
 Type <code>[1]</code>: void </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function is the same as calling ustr_dupx_empty()&nbsp;<wbr>with the current set of default options. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_dupx_undef() <br/>
 Returns: Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Size of allocated storage <br/>
 Type <code>[1]</code>: size_t </p>
<p> <br/>
 Parameter <code>[2]</code>: Number of bytes to use for reference count <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Exact memory allocations <br/>
 Type <code>[3]</code>: int </p>
<p> <br/>
 Parameter <code>[4]</code>: ENOMEM, memory error flag <br/>
 Type <code>[4]</code>: int </p>
<p> <br/>
 Parameter <code>[5]</code>: Length of new undefined data <br/>
 Type <code>[5]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like you called ustr_dupx_empty()&nbsp;<wbr>and then ustr_add_undef(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_dup_undef() <br/>
 Returns: Pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Length of new undefined data <br/>
 Type <code>[1]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function is the same as calling ustr_dupx_undef()&nbsp;<wbr>with the current set of default options. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_dup() <br/>
 Returns: A pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function tries to increase the reference count on the passed Ustr string, and if that succeeds returns that as an argument. If that fails it tries creates a new Ustr string that looks identical to the old Ustr string, apart from the reference count. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>Because the new Ustr string is configured identically to the old Ustr string this means the result can be very different to what you get if you call ustr_dup_buf()&nbsp;<wbr>with ustr_cstr()&nbsp;<wbr>and ustr_len()&nbsp;<wbr>from the original string where the configuration would be whatever the default is. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>Esp. worth of note is that if you ustr_dup()&nbsp;<wbr>a Ustr string with an explicit size of 900 but a length of 1, and the reference count is full the returned Ustr string will have a size of 900 bytes and so will have allocated a little over that. ustr_dup_buf(), even with a sized configuration would only allocate about 12 bytes and have a size a little less than that. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_dupx() <br/>
 Returns: Pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Size of allocated storage <br/>
 Type <code>[1]</code>: size_t </p>
<p> <br/>
 Parameter <code>[2]</code>: Number of bytes to use for reference count <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Exact memory allocations <br/>
 Type <code>[3]</code>: int </p>
<p> <br/>
 Parameter <code>[4]</code>: ENOMEM, memory error flag <br/>
 Type <code>[4]</code>: int </p>
<p> <br/>
 Parameter <code>[5]</code>: Pointer to a constant Ustr string <br/>
 Type <code>[5]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function tries to add a reference if the value of the size, reference bytes, exact memory allocations and ENOMEM are the same as those in the passed Ustr string&nbsp;<wbr>(Parameter[5]). If the comparison fails or the addition of a reference fails it works like ustr_dupx_buf()&nbsp;<wbr>using ustr_cstr()&nbsp;<wbr>and ustr_len(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_dup() <br/>
 Returns: A pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling ustr_dup(), but if the reference count is maxed out then and so a new Ustr string has been allocated then that is stored in the passed argument&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>and the&nbsp;<wbr>&quot;old&quot;&nbsp;<wbr>Ustr string is returned. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>The reason to use this is that if you have a&nbsp;<wbr>&quot;main&quot;&nbsp;<wbr>Ustr string pointer that a lot of things are getting references too then when the reference count maxes out you&#8217;ll degrade into worst case behaviour which acts as though there are no reference counts. This function stops that problem. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>As an example, if you have a 1 byte reference count and have 255&nbsp;<wbr>*&nbsp;<wbr>2 references then using ustr_dup()&nbsp;<wbr>will create 256 Ustr strings using this function will create 4 Ustr strings. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_dupx() <br/>
 Returns: Pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Size of allocated storage <br/>
 Type <code>[1]</code>: size_t </p>
<p> <br/>
 Parameter <code>[2]</code>: Number of bytes to use for reference count <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Exact memory allocations <br/>
 Type <code>[3]</code>: int </p>
<p> <br/>
 Parameter <code>[4]</code>: ENOMEM, memory error flag <br/>
 Type <code>[4]</code>: int </p>
<p> <br/>
 Parameter <code>[5]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[5]</code>: struct Ustr ** </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling ustr_dupx(), but if the reference count is maxed out then and so a new Ustr string is allocated then that is stored in the passed argument&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>and the&nbsp;<wbr>&quot;old&quot;&nbsp;<wbr>Ustr string is returned. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>If the configurations of the new Ustr string and the old Ustr string are not the same, this function works identically to ustr_dupx(). </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>The reason to use this is that if you have a&nbsp;<wbr>&quot;main&quot;&nbsp;<wbr>Ustr string pointer that a lot of things are getting references too then when the reference count maxes out you&#8217;ll degrade into worst case behaviour which acts as though there are no reference counts. This function stops that problem. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>As an example, if you have a 1 byte reference count and have 255&nbsp;<wbr>*&nbsp;<wbr>2 references then using ustr_dupx()&nbsp;<wbr>will create 256 Ustr strings using this function will create 4 Ustr strings. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_dup_buf() <br/>
 Returns: A pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to data <br/>
 Type <code>[1]</code>: const void * </p>
<p> <br/>
 Parameter <code>[2]</code>: Length of data <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_dup_undef()&nbsp;<wbr>and then copied the data into the new undefined space. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_dupx_buf() <br/>
 Returns: Pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Size of allocated storage <br/>
 Type <code>[1]</code>: size_t </p>
<p> <br/>
 Parameter <code>[2]</code>: Number of bytes to use for reference count <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Exact memory allocations <br/>
 Type <code>[3]</code>: int </p>
<p> <br/>
 Parameter <code>[4]</code>: ENOMEM, memory error flag <br/>
 Type <code>[4]</code>: int </p>
<p> <br/>
 Parameter <code>[5]</code>: Pointer to data <br/>
 Type <code>[5]</code>: const void * </p>
<p> <br/>
 Parameter <code>[6]</code>: Length of data <br/>
 Type <code>[6]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_dupx_undef()&nbsp;<wbr>and then copied the data into the new undefined space. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_dup_cstr() <br/>
 Returns: A pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to constant C-style string <br/>
 Type <code>[1]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_dup_buf()&nbsp;<wbr>and passed strlen()&nbsp;<wbr>as the length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_dupx_cstr() <br/>
 Returns: Pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Size of allocated storage <br/>
 Type <code>[1]</code>: size_t </p>
<p> <br/>
 Parameter <code>[2]</code>: Number of bytes to use for reference count <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Exact memory allocations <br/>
 Type <code>[3]</code>: int </p>
<p> <br/>
 Parameter <code>[4]</code>: ENOMEM, memory error flag <br/>
 Type <code>[4]</code>: int </p>
<p> <br/>
 Parameter <code>[5]</code>: Pointer to constant C-style string <br/>
 Type <code>[5]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_dupx_buf()&nbsp;<wbr>and passed strlen()&nbsp;<wbr>as the length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR_DUP_OSTR() <br/>
 Returns: A pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: A constant C-style string <br/>
 Type <code>[1]</code>: const char [] </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_dup_buf()&nbsp;<wbr>and passed sizeof()&nbsp;<wbr>- 1 as the length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR_DUP_OBJ() <br/>
 Returns: A pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: A symbol <br/>
 Type <code>[1]</code>: ... </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_dup_buf()&nbsp;<wbr>and passed sizeof()&nbsp;<wbr>as the length. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>In most cases you&#8217;ll want to use USTR_DUP_OSTR(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_dup_subustr() <br/>
 Returns: A pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Position in the Ustr <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Length to add from the Ustr <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function mostly works as if you had called ustr_dup_buf()&nbsp;<wbr>with the ustr_cstr()&nbsp;<wbr>+&nbsp;<wbr>position - 1 and length values of the Ustr string to be added. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>If the position is 1 and the length is the length of the Ustr string then it just calls ustr_dup(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_dupx_subustr() <br/>
 Returns: Pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Size of allocated storage <br/>
 Type <code>[1]</code>: size_t </p>
<p> <br/>
 Parameter <code>[2]</code>: Number of bytes to use for reference count <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Exact memory allocations <br/>
 Type <code>[3]</code>: int </p>
<p> <br/>
 Parameter <code>[4]</code>: ENOMEM, memory error flag <br/>
 Type <code>[4]</code>: int </p>
<p> <br/>
 Parameter <code>[5]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[5]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[6]</code>: Position in the Ustr <br/>
 Type <code>[6]</code>: size_t </p>
<p> <br/>
 Parameter <code>[7]</code>: Length to add from the Ustr <br/>
 Type <code>[7]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function mostly works as if you had called ustr_dupx_buf()&nbsp;<wbr>with the ustr_cstr()&nbsp;<wbr>+&nbsp;<wbr>position - 1 and length values of the Ustr string to be added. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>If the position is 1 and the length is the length of the Ustr string then it just calls ustr_dupx(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_dup_rep_chr() <br/>
 Returns: A pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Byte value of data <br/>
 Type <code>[1]</code>: char </p>
<p> <br/>
 Parameter <code>[2]</code>: Length of bytes as data <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_dup_undef()&nbsp;<wbr>and then copied the byte value to each position. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_dupx_rep_chr() <br/>
 Returns: Pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Size of allocated storage <br/>
 Type <code>[1]</code>: size_t </p>
<p> <br/>
 Parameter <code>[2]</code>: Number of bytes to use for reference count <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Exact memory allocations <br/>
 Type <code>[3]</code>: int </p>
<p> <br/>
 Parameter <code>[4]</code>: ENOMEM, memory error flag <br/>
 Type <code>[4]</code>: int </p>
<p> <br/>
 Parameter <code>[5]</code>: Byte value of data <br/>
 Type <code>[5]</code>: char </p>
<p> <br/>
 Parameter <code>[6]</code>: Length of bytes as data <br/>
 Type <code>[6]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_dupx_undef()&nbsp;<wbr>and then copied the byte value to each position. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_vjoin() <br/>
 Returns: Pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Separator to go between Ustr strings <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to the first constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to the second constant Ustr string <br/>
 Type <code>[3]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[4]</code>: Variable argument list variable, from va_start() <br/>
 Type <code>[4]</code>: va_list </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you called ustr_dup()&nbsp;<wbr>on the first Ustr string&nbsp;<wbr>(Parameter[2]), and then ustr_add()&nbsp;<wbr>on the separator&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>followed by ustr_add()&nbsp;<wbr>on the second Ustr string&nbsp;<wbr>(Parameter[3]). This process then repeats for all the Ustr strings in the variable argument list&nbsp;<wbr>(Parameter[4])&nbsp;<wbr>until a USTR_NULL is reached. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function doesn&#8217;t guarantee to just take a reference to one of the passed Ustr strings, even if that is what would happen if you called the above manually. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_join() <br/>
 Returns: Pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Separator to go between Ustr strings <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to the first constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to the second constant Ustr string <br/>
 Type <code>[3]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[4]</code>: Zero or more pointers to constant Ustr strings and then USTR_NULL <br/>
 Type <code>[4]</code>: ... </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function calls va_start()&nbsp;<wbr>to get a variable argument list and then calls ustr_sc_vjoin(). </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function doesn&#8217;t guarantee to just take a reference to one of the passed Ustr strings, even if that is what would happen if you called the above manually. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_vjoinx() <br/>
 Returns: Pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Size of allocated storage <br/>
 Type <code>[1]</code>: size_t </p>
<p> <br/>
 Parameter <code>[2]</code>: Number of bytes to use for reference count <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Exact memory allocations <br/>
 Type <code>[3]</code>: int </p>
<p> <br/>
 Parameter <code>[4]</code>: ENOMEM, memory error flag <br/>
 Type <code>[4]</code>: int </p>
<p> <br/>
 Parameter <code>[5]</code>: Separator to go between Ustr strings <br/>
 Type <code>[5]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[6]</code>: A pointer to the first constant Ustr string <br/>
 Type <code>[6]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[7]</code>: A pointer to the second constant Ustr string <br/>
 Type <code>[7]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[8]</code>: Variable argument list variable, from va_start() <br/>
 Type <code>[8]</code>: va_list </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you called ustr_dupx()&nbsp;<wbr>on the first Ustr string&nbsp;<wbr>(Parameter[2]), and then ustr_add()&nbsp;<wbr>on the separator&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>followed by ustr_add()&nbsp;<wbr>on the second Ustr string&nbsp;<wbr>(Parameter[3]). This process then repeats for all the Ustr strings in the variable argument list&nbsp;<wbr>(Parameter[4])&nbsp;<wbr>until a USTR_NULL is reached. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function doesn&#8217;t guarantee to just take a reference to one of the passed Ustr strings, even if that is what would happen if you called the above manually. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_joinx() <br/>
 Returns: Pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Size of allocated storage <br/>
 Type <code>[1]</code>: size_t </p>
<p> <br/>
 Parameter <code>[2]</code>: Number of bytes to use for reference count <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Exact memory allocations <br/>
 Type <code>[3]</code>: int </p>
<p> <br/>
 Parameter <code>[4]</code>: ENOMEM, memory error flag <br/>
 Type <code>[4]</code>: int </p>
<p> <br/>
 Parameter <code>[5]</code>: Separator to go between Ustr strings <br/>
 Type <code>[5]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[6]</code>: A pointer to the first constant Ustr string <br/>
 Type <code>[6]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[7]</code>: A pointer to the second constant Ustr string <br/>
 Type <code>[7]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[8]</code>: Zero or more pointers to constant Ustr strings and then USTR_NULL <br/>
 Type <code>[8]</code>: ... </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function calls va_start()&nbsp;<wbr>to get a variable argument list and then calls ustr_sc_vjoinx(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_vconcat() <br/>
 Returns: Pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to the first constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Variable argument list variable, from va_start() <br/>
 Type <code>[2]</code>: va_list </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you called ustr_dup()&nbsp;<wbr>on the first Ustr string&nbsp;<wbr>(Parameter[1]), and then ustr_add()&nbsp;<wbr>on the second Ustr string&nbsp;<wbr>(Parameter[3]). This process then repeats for all the Ustr strings in the variable argument list&nbsp;<wbr>(Parameter[4])&nbsp;<wbr>until a USTR_NULL is reached. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function doesn&#8217;t guarantee to just take a reference to one of the passed Ustr strings, even if that is what would happen if you called the above manually. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_concat() <br/>
 Returns: Pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to the first constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Zero or more pointers to constant Ustr strings and then USTR_NULL <br/>
 Type <code>[2]</code>: ... </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function calls va_start()&nbsp;<wbr>to get a variable argument list and then calls ustr_sc_vconcat(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_vconcatx() <br/>
 Returns: Pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Size of allocated storage <br/>
 Type <code>[1]</code>: size_t </p>
<p> <br/>
 Parameter <code>[2]</code>: Number of bytes to use for reference count <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Exact memory allocations <br/>
 Type <code>[3]</code>: int </p>
<p> <br/>
 Parameter <code>[4]</code>: ENOMEM, memory error flag <br/>
 Type <code>[4]</code>: int </p>
<p> <br/>
 Parameter <code>[5]</code>: A pointer to the first constant Ustr string <br/>
 Type <code>[5]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[6]</code>: Variable argument list variable, from va_start() <br/>
 Type <code>[6]</code>: va_list </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you called ustr_dupx()&nbsp;<wbr>on the first Ustr string&nbsp;<wbr>(Parameter[1]), and then ustr_add()&nbsp;<wbr>on the second Ustr string&nbsp;<wbr>(Parameter[3]). This process then repeats for all the Ustr strings in the variable argument list&nbsp;<wbr>(Parameter[4])&nbsp;<wbr>until a USTR_NULL is reached. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function doesn&#8217;t guarantee to just take a reference to one of the passed Ustr strings, even if that is what would happen if you called the above manually. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_concatx() <br/>
 Returns: Pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Size of allocated storage <br/>
 Type <code>[1]</code>: size_t </p>
<p> <br/>
 Parameter <code>[2]</code>: Number of bytes to use for reference count <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Exact memory allocations <br/>
 Type <code>[3]</code>: int </p>
<p> <br/>
 Parameter <code>[4]</code>: ENOMEM, memory error flag <br/>
 Type <code>[4]</code>: int </p>
<p> <br/>
 Parameter <code>[5]</code>: A pointer to the first constant Ustr string <br/>
 Type <code>[5]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[6]</code>: Zero or more pointers to constant Ustr strings and then USTR_NULL <br/>
 Type <code>[6]</code>: ... </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function calls va_start()&nbsp;<wbr>to get a variable argument list and then calls ustr_sc_vconcatx(). </p>
<h2>Deleting a Ustr, or data within a Ustr</h2>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_free() <br/>
 Returns: Nothing <br/>
 Type: void </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a Ustr <br/>
 Type <code>[1]</code>: struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function decrements the reference count on a Ustr, if there is one, and free&#8217;s it if it is allocated and the reference count becomes zero. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function does nothing if passed USTR_NULL. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustrp_free() <br/>
 Returns: Nothing <br/>
 Type: void </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a Ustr pool object <br/>
 Type <code>[1]</code>: struct Ustr_pool * </p>
<p> <br/>
 Parameter <code>[2]</code>: Pointer to a Ustrp (pool allocated Ustr) <br/>
 Type <code>[2]</code>: struct Ustrp * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_free()&nbsp;<wbr>but calls the pool_free member function of the Ustr_pool&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>instead of the ustr system free. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_free() <br/>
 Returns: Nothing <br/>
 Type: void </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function calls ustr_free()&nbsp;<wbr>and then sets the pointer&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>to USTR_NULL, which is a noop when passed to ustr_free(). This can be used to help prevent&nbsp;<wbr>&quot;double free&quot;&nbsp;<wbr>errors. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>While the point to the pointer must be non-NULL, this function also accepts a NULL ustr and does nothing. So you can pass the same pointer to this function multiple times and only the first one will do anything. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_free2() <br/>
 Returns: Nothing <br/>
 Type: void </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Pointer to a Ustr string <br/>
 Type <code>[2]</code>: struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_sc_free()&nbsp;<wbr>but instead of setting the pointer&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>to USTR_NULL it sets it to the Ustr string&nbsp;<wbr>(Parameter[2]). </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>While the point to the pointer must be non-NULL, this function also accepts a NULL ustr to be free&#8217;d and does nothing. So you can pass the same pointer to ustr_sc_free()&nbsp;<wbr>and then this function safely. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>The passed value&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>shouldn&#8217;t be USTR_NULL, and in debugging mode the function will assert()&nbsp;<wbr>that it isn&#8217;t. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_free_shared() <br/>
 Returns: Nothing <br/>
 Type: void </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function is a simple way to&nbsp;<wbr>&quot;free&quot;&nbsp;<wbr>a Ustr string that has been shared&nbsp;<wbr>(ustr_shared()&nbsp;<wbr>returns USTR_TRUE), normally ustr_free()&nbsp;<wbr>is ignored on a shared Ustr string. It just calls ustr_setf_owner()&nbsp;<wbr>and then ustr_sc_free(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_del() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Length to delete from the Ustr <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function deletes data from the end of Ustr, possibly re-sizing the Ustr at the same time. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>The Ustr is never re-sized when the size is stored explicitly, so the pointer never changes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_del_subustr() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position in the Ustr <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Length to delete from the Ustr <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_del()&nbsp;<wbr>but can delete an arbitrary section of the Ustr. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_del() <br/>
 Returns: Nothing <br/>
 Type: void </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function is like calling ustr_del()&nbsp;<wbr>with ustr_len()&nbsp;<wbr>as the length, however if that fails it does a ustr_free()&nbsp;<wbr>and then sets the pointer to USTR(&quot;&quot;). </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>While the benifit is that you don&#8217;t have to check for memory failure errors, if there is a memory failure and you have a non-default configuration the configuration will revert back to the default. </p>
<h2>Adding data to a Ustr</h2>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_add_undef() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Length of new undefined data <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>The Ustr string is expanded&nbsp;<wbr>(possibly reallocated)&nbsp;<wbr>so that it can contain length&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>extra data, if the length is not zero the Ustr will be writable. Or it&#8217;ll return USTR_FALSE&nbsp;<wbr>(zero)&nbsp;<wbr>on failure. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_add_buf() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Pointer to data <br/>
 Type <code>[2]</code>: const void * </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of data <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_add_undef()&nbsp;<wbr>and then copied the data into the new undefined space. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_add_cstr() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Pointer to constant C-style string <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_add_buf()&nbsp;<wbr>and passed strlen()&nbsp;<wbr>as the length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR_ADD_OSTR() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A constant C-style string <br/>
 Type <code>[2]</code>: const char [] </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_add_buf()&nbsp;<wbr>and passed sizeof()&nbsp;<wbr>- 1 as the length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR_ADD_OBJ() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A symbol <br/>
 Type <code>[2]</code>: ... </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_add_buf()&nbsp;<wbr>and passed sizeof()&nbsp;<wbr>as the length. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>In most cases you&#8217;ll want to use USTR_ADD_OSTR(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_add() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function mostly works as if you had called ustr_add_buf()&nbsp;<wbr>with the ustr_cstr()&nbsp;<wbr>and ustr_len()&nbsp;<wbr>values of the Ustr string to be added. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>If the Ustr string is zero length and isn&#8217;t writable this function may just add a reference, this is fine for Ustr strings that are&nbsp;<wbr>&quot;constant&quot;&nbsp;<wbr>because if the Ustr is read-only then the memory will not be written to. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_add_subustr() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[3]</code>: Position in the Ustr <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: Length to add from the Ustr <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function mostly works as if you had called ustr_add_buf()&nbsp;<wbr>with the ustr_cstr()&nbsp;<wbr>+&nbsp;<wbr>position - 1 and length values of the Ustr string to be added. The exception being if you add a ustr to itself, while only having a single reference count, the simple method would access a free&#8217;d ustr, but this function just works. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>If the position is 1 and the length is the length of the Ustr string then it just calls ustr_add(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_add_rep_chr() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Byte value of data <br/>
 Type <code>[2]</code>: char </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of bytes as data <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_add_undef()&nbsp;<wbr>and then copied the byte value to each position. </p>
<h2>Setting a Ustr to some data</h2>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_set_undef() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: size_t <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_del()&nbsp;<wbr>for the entire string and the ustr_add_undef(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_set_empty() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_del()&nbsp;<wbr>for the entire string, however the string will be allocated if this completes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_set_buf() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Buffer containting data <br/>
 Type <code>[2]</code>: const void * </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of Buffer <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_del()&nbsp;<wbr>for the entire string and the ustr_add_buf(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_set_cstr() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant C-style string <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_del()&nbsp;<wbr>for the entire string and then ustr_add_cstr(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR_SET_OSTR() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A constant C-style string <br/>
 Type <code>[2]</code>: const char [] </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_del()&nbsp;<wbr>for the entire string and then USTR_ADD_OSTR(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR_SET_OBJ() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A symbol <br/>
 Type <code>[2]</code>: ... </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_del()&nbsp;<wbr>for the entire string and then USTR_ADD_OBJ(). </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>In most cases you&#8217;ll want to use USTR_SET_OSTR(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_set() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_del()&nbsp;<wbr>for the entire string and the ustr_add(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_set_subustr() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[3]</code>: Position in the Ustr <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: Length to set from the Ustr <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_del()&nbsp;<wbr>for the entire string and the ustr_add_subustr(). The exception being if you set a ustr to itself, while only having a single reference count, the simple method would access a free&#8217;d ustr data, but this function just works. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_set_rep_chr() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Byte value of data <br/>
 Type <code>[2]</code>: char </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of bytes as data <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_del()&nbsp;<wbr>for the entire string and the ustr_add_rep_chr(). </p>
<h2>Inserting data into a Ustr</h2>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_ins_undef() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position after which the data should be added <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of new undefined data <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>The Ustr string is expanded&nbsp;<wbr>(possibly reallocated)&nbsp;<wbr>so that it can contain length&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>extra data, from after the required position. If the length is not zero the Ustr will be writable. Or it&#8217;ll return USTR_FALSE&nbsp;<wbr>(zero)&nbsp;<wbr>on failure. The data in the Ustr is moved as needed to put the new data at position&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>+&nbsp;<wbr>1. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_ins_buf() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position after which the data should be added <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Pointer to data <br/>
 Type <code>[3]</code>: const void * </p>
<p> <br/>
 Parameter <code>[4]</code>: Length of data <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_ins_undef()&nbsp;<wbr>and then copied the data into the new undefined space. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_ins_cstr() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position after which the data should be added <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Pointer to constant C-style string <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_ins_buf()&nbsp;<wbr>and passed strlen()&nbsp;<wbr>as the length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR_INS_OSTR() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position after which the data should be added <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A constant C-style string <br/>
 Type <code>[3]</code>: const char [] </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_ins_buf()&nbsp;<wbr>and passed sizeof()&nbsp;<wbr>- 1 as the length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR_INS_OBJ() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position after which the data should be added <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A symbol <br/>
 Type <code>[3]</code>: ... </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_ins_buf()&nbsp;<wbr>and passed sizeof()&nbsp;<wbr>as the length. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>In most cases you&#8217;ll want to use USTR_INS_OSTR(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_ins() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position after which the data should be added <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[3]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_ins_buf()&nbsp;<wbr>with the ustr_cstr()&nbsp;<wbr>and ustr_len()&nbsp;<wbr>values of the Ustr string to be added. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_ins_subustr() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position after which the data should be added <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[3]</code>: Position in the Ustr <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: Length to ins from the Ustr <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function mostly as if you had called ustr_ins_buf()&nbsp;<wbr>with the ustr_cstr()&nbsp;<wbr>+&nbsp;<wbr>position - 1 and length values of the Ustr string to be insed. The exception being if you insert a ustr to itself, while only having a single reference count, the simple method would access a free&#8217;d ustr data, but this function just works. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_ins_rep_chr() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position after which the data should be added <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[2]</code>: Byte value of data <br/>
 Type <code>[2]</code>: char </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of bytes as data <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_ins_undef()&nbsp;<wbr>and then copied the byte value to each position. </p>
<h2>Adding, duplicating and setting formatted data to a Ustr</h2>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_add_vfmt_lim() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Limit of data to add <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant C-style string <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 Parameter <code>[4]</code>: Variable argument list variable, from va_start() <br/>
 Type <code>[4]</code>: va_list </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling the system vsnprintf()&nbsp;<wbr>with the limit&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>as the limit to vsnprintf()&nbsp;<wbr>and then calling ustr_add_buf(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_add_vfmt() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant C-style string <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 Parameter <code>[3]</code>: Variable argument list variable, from va_start() <br/>
 Type <code>[3]</code>: va_list </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling the system vsnprintf()&nbsp;<wbr>and then calling ustr_add_buf(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_add_fmt_lim() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Limit of data to add <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant C-style string <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 Parameter <code>[4]</code>: Options depending on value of Parameter[3] <br/>
 Type <code>[4]</code>: ... </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling the system snprintf()&nbsp;<wbr>with the limit&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>as the limit to snprintf()&nbsp;<wbr>and then calling ustr_add_buf(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_add_fmt() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant C-style string <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 Parameter <code>[3]</code>: Options depending on value of Parameter[2] <br/>
 Type <code>[3]</code>: ... </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling the system snprintf()&nbsp;<wbr>and then calling ustr_add_buf(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_dup_vfmt_lim() <br/>
 Returns: Pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Limit of data to dup <br/>
 Type <code>[1]</code>: size_t </p>
<p> <br/>
 Parameter <code>[2]</code>: Pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 Parameter <code>[3]</code>: Variable argument list variable, from va_start() <br/>
 Type <code>[3]</code>: va_list </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling the system vsnprintf()&nbsp;<wbr>with the limit&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>as the limit to vsnprintf()&nbsp;<wbr>and then calling ustr_dup_buf(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_dup_vfmt() <br/>
 Returns: Pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Limit of data to dup <br/>
 Type <code>[1]</code>: size_t </p>
<p> <br/>
 Parameter <code>[2]</code>: Pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 Parameter <code>[3]</code>: Variable argument list variable, from va_start() <br/>
 Type <code>[3]</code>: va_list </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling the system vsnprintf()&nbsp;<wbr>and then calling ustr_dup_buf(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_dup_fmt_lim() <br/>
 Returns: Pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Limit of data to dup <br/>
 Type <code>[1]</code>: size_t </p>
<p> <br/>
 Parameter <code>[2]</code>: Pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 Parameter <code>[3]</code>: Options depending on value of Parameter[2] <br/>
 Type <code>[3]</code>: ... </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling the system snprintf()&nbsp;<wbr>with the limit&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>as the limit to snprintf()&nbsp;<wbr>and then calling ustr_dup_buf(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_dup_fmt() <br/>
 Returns: Pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const char * </p>
<p> <br/>
 Parameter <code>[2]</code>: Options depending on value of Parameter[1] <br/>
 Type <code>[2]</code>: ... </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling the system snprintf()&nbsp;<wbr>and then calling ustr_dup_buf(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_dupx_fmt_lim() <br/>
 Returns: Pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Size of allocated storage <br/>
 Type <code>[1]</code>: size_t </p>
<p> <br/>
 Parameter <code>[2]</code>: Number of bytes to use for reference count <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Exact memory allocations <br/>
 Type <code>[3]</code>: int </p>
<p> <br/>
 Parameter <code>[4]</code>: ENOMEM, memory error flag <br/>
 Type <code>[4]</code>: int </p>
<p> <br/>
 Parameter <code>[5]</code>: Limit of data to dup <br/>
 Type <code>[5]</code>: size_t </p>
<p> <br/>
 Parameter <code>[6]</code>: Pointer to a constant Ustr string <br/>
 Type <code>[6]</code>: const char * </p>
<p> <br/>
 Parameter <code>[7]</code>: Options depending on value of Parameter[6] <br/>
 Type <code>[7]</code>: ... </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling the system snprintf()&nbsp;<wbr>with the limit&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>as the limit to snprintf()&nbsp;<wbr>and then calling ustr_dupx_buf(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_dupx_fmt() <br/>
 Returns: Pointer to a Ustr string <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Size of allocated storage <br/>
 Type <code>[1]</code>: size_t </p>
<p> <br/>
 Parameter <code>[2]</code>: Number of bytes to use for reference count <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Exact memory allocations <br/>
 Type <code>[3]</code>: int </p>
<p> <br/>
 Parameter <code>[4]</code>: ENOMEM, memory error flag <br/>
 Type <code>[4]</code>: int </p>
<p> <br/>
 Parameter <code>[5]</code>: Pointer to a constant Ustr string <br/>
 Type <code>[5]</code>: const char * </p>
<p> <br/>
 Parameter <code>[6]</code>: Options depending on value of Parameter[5] <br/>
 Type <code>[6]</code>: ... </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling the system snprintf()&nbsp;<wbr>and then calling ustr_dup_bufx(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_set_vfmt_lim() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Limit of data to set <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant C-style string <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 Parameter <code>[4]</code>: Variable argument list variable, from va_start() <br/>
 Type <code>[4]</code>: va_list </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling ustr_del()&nbsp;<wbr>for all the data and then ustr_add_vfmt_lim(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_set_vfmt() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant C-style string <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 Parameter <code>[3]</code>: Variable argument list variable, from va_start() <br/>
 Type <code>[3]</code>: va_list </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling ustr_del()&nbsp;<wbr>for all the data and then ustr_add_vfmt(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_set_fmt_lim() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Limit of data to set <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant C-style string <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 Parameter <code>[4]</code>: Options depending on value of Parameter[3] <br/>
 Type <code>[4]</code>: ... </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling ustr_del()&nbsp;<wbr>for all the data and then ustr_add_fmt_lim(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_set_fmt() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant C-style string <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 Parameter <code>[3]</code>: Options depending on value of Parameter[2] <br/>
 Type <code>[3]</code>: ... </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling ustr_del()&nbsp;<wbr>for all the data and then ustr_add_fmt(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_ins_vfmt_lim() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position after which the data should be added <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Limit of data to insert <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: A pointer to a constant C-style string <br/>
 Type <code>[4]</code>: const char * </p>
<p> <br/>
 Parameter <code>[5]</code>: Variable argument list variable, from va_start() <br/>
 Type <code>[5]</code>: va_list </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling the system vsnprintf()&nbsp;<wbr>with the limit&nbsp;<wbr>(Parameter[3])&nbsp;<wbr>as the limit to vsnprintf()&nbsp;<wbr>and then calling ustr_ins_buf(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_ins_vfmt() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position after which the data should be added <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant C-style string <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 Parameter <code>[4]</code>: Variable argument list variable, from va_start() <br/>
 Type <code>[4]</code>: va_list </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling the system vsnprintf()&nbsp;<wbr>and then calling ustr_ins_buf(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_ins_fmt_lim() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position after which the data should be added <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Limit of data to insert <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: A pointer to a constant C-style string <br/>
 Type <code>[4]</code>: const char * </p>
<p> <br/>
 Parameter <code>[5]</code>: Options depending on value of Parameter[4] <br/>
 Type <code>[5]</code>: ... </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling the system snprintf()&nbsp;<wbr>with the limit&nbsp;<wbr>(Parameter[3])&nbsp;<wbr>as the limit to snprintf()&nbsp;<wbr>and then calling ustr_ins_buf(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_ins_fmt() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position after which the data should be added <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant C-style string <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 Parameter <code>[4]</code>: Options depending on value of Parameter[3] <br/>
 Type <code>[4]</code>: ... </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling the system snprintf()&nbsp;<wbr>and then calling ustr_ins_buf(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sub_vfmt_lim() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position where to start substitution <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Limit of data to substitute <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: A pointer to a constant C-style string <br/>
 Type <code>[4]</code>: const char * </p>
<p> <br/>
 Parameter <code>[5]</code>: Variable argument list variable, from va_start() <br/>
 Type <code>[5]</code>: va_list </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling the system vsnprintf()&nbsp;<wbr>with the limit&nbsp;<wbr>(Parameter[3])&nbsp;<wbr>as the limit to vsnprintf()&nbsp;<wbr>and then calling ustr_sub_buf(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sub_vfmt() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position where to start substitution <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant C-style string <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 Parameter <code>[4]</code>: Variable argument list variable, from va_start() <br/>
 Type <code>[4]</code>: va_list </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling the system vsnprintf()&nbsp;<wbr>and then calling ustr_sub_buf(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sub_fmt_lim() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position where to start substitution <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Limit of data to substitute <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: A pointer to a constant C-style string <br/>
 Type <code>[4]</code>: const char * </p>
<p> <br/>
 Parameter <code>[5]</code>: Options depending on value of Parameter[4] <br/>
 Type <code>[5]</code>: ... </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling the system snprintf()&nbsp;<wbr>with the limit&nbsp;<wbr>(Parameter[3])&nbsp;<wbr>as the limit to snprintf()&nbsp;<wbr>and then calling ustr_sub_buf(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sub_fmt() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position where to start substitution <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant C-style string <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 Parameter <code>[4]</code>: Options depending on value of Parameter[3] <br/>
 Type <code>[4]</code>: ... </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling the system snprintf()&nbsp;<wbr>and then calling ustr_sub_buf(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_sub_vfmt_lim() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position where to start substitution <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of substitution <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: Limit of data to substitute <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 Parameter <code>[5]</code>: A pointer to a constant C-style string <br/>
 Type <code>[5]</code>: const char * </p>
<p> <br/>
 Parameter <code>[6]</code>: Variable argument list variable, from va_start() <br/>
 Type <code>[6]</code>: va_list </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling the system vsnprintf()&nbsp;<wbr>with the limit&nbsp;<wbr>(Parameter[4])&nbsp;<wbr>as the limit to vsnprintf()&nbsp;<wbr>and then calling ustr_sc_sub_buf(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_sub_vfmt() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position where to start substitution <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of substitution <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: A pointer to a constant C-style string <br/>
 Type <code>[4]</code>: const char * </p>
<p> <br/>
 Parameter <code>[5]</code>: Variable argument list variable, from va_start() <br/>
 Type <code>[5]</code>: va_list </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling the system vsnprintf()&nbsp;<wbr>and then calling ustr_sc_sub_buf(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_sub_fmt_lim() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position where to start substitution <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of substitution <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: Limit of data to substitute <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 Parameter <code>[5]</code>: A pointer to a constant C-style string <br/>
 Type <code>[5]</code>: const char * </p>
<p> <br/>
 Parameter <code>[6]</code>: Options depending on value of Parameter[5] <br/>
 Type <code>[6]</code>: ... </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling the system snprintf()&nbsp;<wbr>with the limit&nbsp;<wbr>(Parameter[3])&nbsp;<wbr>as the limit to snprintf()&nbsp;<wbr>and then calling ustr_sc_sub_buf(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_sub_fmt() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position where to start substitution <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of substitution <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: A pointer to a constant C-style string <br/>
 Type <code>[4]</code>: const char * </p>
<p> <br/>
 Parameter <code>[5]</code>: Options depending on value of Parameter[5] <br/>
 Type <code>[5]</code>: ... </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling the system snprintf()&nbsp;<wbr>and then calling ustr_sc_sub_buf(). </p>
<h2>Accessing the variables of a Ustr</h2>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_len() <br/>
 Returns: The length of the Ustr <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function returns the length of the data within the Ustr, much like strlen()&nbsp;<wbr>but without getting the value wrong in the case of extra NIL bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cstr() <br/>
 Returns: Read-only pointer to the start of data in the Ustr <br/>
 Type: const char * </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function returns a read-only pointer to the start of the data of the Ustr string. Due to there always being a terminating NIL byte in a Ustr, this is also a valid C-style string. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_wstr() <br/>
 Returns: Writable pointer to the start of data in the Ustr, or NULL <br/>
 Type: char * </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function returns a writable pointer to the start of the data of the Ustr string. Due to there always being a terminating NIL byte in a Ustr, this is also a valid C-style string. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>If the ustr is read-only&nbsp;<wbr>(ustr_ro()&nbsp;<wbr>==&nbsp;<wbr>USTR_TRUE)&nbsp;<wbr>then this function will return NULL. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>Unless the string is owned&nbsp;<wbr>(ustr_owner()&nbsp;<wbr>==&nbsp;<wbr>USTR_TRUE)&nbsp;<wbr>it can be a very bad idea to use this to change data, as then all references will be updated. See ustr_sc_wstr(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_alloc() <br/>
 Returns: A boolean flag of either USTR_TRUE or USTR_FALSE <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function says if the Ustr is currently in allocated storage. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_exact() <br/>
 Returns: A boolean flag of either USTR_TRUE or USTR_FALSE <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function says if the Ustr is doing exact allocations, so as the Ustr grows it will only have storage allocated exactly as required and not in half powers of two. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This will always be USTR_FALSE for read-only Ustr strings&nbsp;<wbr>(ustr_ro()&nbsp;<wbr>==&nbsp;<wbr>USTR_TRUE), even though the default may be to used exact sized allocations when&nbsp;<wbr>&nbsp;<wbr>adding data to them etc. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sized() <br/>
 Returns: A boolean flag of either USTR_TRUE or USTR_FALSE <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function says if the Ustr stores an explicit allocation size, if not the size is implied as the next highest half power of two. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_ro() <br/>
 Returns: A boolean flag of either USTR_TRUE or USTR_FALSE <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function says if the Ustr is current in read-only storage. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>Read-only storage is not writable but can be referenced via. ustr_dup()&nbsp;<wbr>an infinite amount of times. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_fixed() <br/>
 Returns: A boolean flag of either USTR_TRUE or USTR_FALSE <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function says if the Ustr is current in fixed size storage. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>Fixed size storage is writable but cannot be referenced. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>Fixed size storage always explicitly stores the size of the storage. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_enomem() <br/>
 Returns: A boolean flag of either USTR_TRUE or USTR_FALSE <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function just returns the value of the user settable flag in the Ustr. It can be set via. ustr_setf_enomem_err()&nbsp;<wbr>and cleared by ustr_setf_enomem_clr(). <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function is automatically set to on whever a memory allocation failure happens for a Ustr. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>If a Ustr is referenced multiple times, ustr_setf_enomem_err()&nbsp;<wbr>will fail. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This always fails for Ustr&#8217;s in read-only storage. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_shared() <br/>
 Returns: A boolean flag of either USTR_TRUE or USTR_FALSE <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function says if the Ustr is in the&nbsp;<wbr>&quot;shared&quot;&nbsp;<wbr>mode. It can be set via. ustr_setf_shared()&nbsp;<wbr>and cleared by ustr_setf_owner()&nbsp;<wbr>on allocated Ustr&#8217;s. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>Shared mode means that a Ustr can be referenced and unreferenced an infinite number of times. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This always succeeds for Ustr&#8217;s in read-only storage. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This always fails for Ustr&#8217;s in fixed size storage. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_limited() <br/>
 Returns: A boolean flag of either USTR_TRUE or USTR_FALSE <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function says if the Ustr is currently in fixed size storage and cannot move to allocated storage. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This always fails for Ustr&#8217;s in allocated storage. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This always fails for Ustr&#8217;s in read-only storage. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_owner() <br/>
 Returns: A boolean flag of either USTR_TRUE or USTR_FALSE <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function says if there is only a single reference to the Ustr string. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This always fails for Ustr&#8217;s in read-only storage. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This always succeeds for Ustr&#8217;s in fixed size storage. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_size() <br/>
 Returns: size_t <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function calculates the maximum amount of data that could be stored&nbsp;<wbr>(Ie. the max ustr_len())&nbsp;<wbr>without having to re-size the Ustr string. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_size_alloc() <br/>
 Returns: size_t <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function returns the size of the storage for the Ustr. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_size_overhead() <br/>
 Returns: size_t <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function returns the difference between the size of the storage and the maximum amount of data that could be stored without having to re-size the Ustr string. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_conf() <br/>
 Returns: Nothing <br/>
 Type: void </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Return size allocated number <br/>
 Type <code>[2]</code>: size_t * </p>
<p> <br/>
 Parameter <code>[3]</code>: Return number of bytes used in the reference count <br/>
 Type <code>[3]</code>: size_t * </p>
<p> <br/>
 Parameter <code>[4]</code>: Return exact allocations flag <br/>
 Type <code>[4]</code>: int * </p>
<p> <br/>
 Parameter <code>[5]</code>: Return number of bytes used in the length <br/>
 Type <code>[5]</code>: size_t * </p>
<p> <br/>
 Parameter <code>[5]</code>: Return number of references to this Ustr <br/>
 Type <code>[5]</code>: size_t * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function gives the configuration of the current Ustr needed to duplicate it via. the ustr_dupx_*()&nbsp;<wbr>functions. It also gives the number of bytes used for the length and the number of references, which are mainly informational. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function differs from calling the ustr_exact()&nbsp;<wbr>etc. functions in that it returns the global options if this Ustr isn&#8217;t allocated, thus telling you what the configuration would be if the Ustr was turned into an allocated Ustr by adding data etc. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>Zero references for an allocated Ustr with a non-zero number of bytes for a reference count means it&#8217;s in&nbsp;<wbr>&quot;shared&quot;&nbsp;<wbr>mode). </p>
<h2>Setting the flags of a Ustr</h2>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_setf_enomem_err() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function sets the enomem flag, which can be observed via. the ustr_enomem()&nbsp;<wbr>function. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>The implication of setting this flag is that a memory error has occured in a previous function call on this Ustr. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function fails if ustr_owner()&nbsp;<wbr>fails for the Ustr. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_setf_enomem_clr() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function clears the enomem flag, which can be observed via. the ustr_enomem()&nbsp;<wbr>function. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>The implication of this flag being set is that a memory error has occured in a previous function call on this Ustr, so on clearing the flag you should know you have brought the Ustr back to a known state. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function fails if ustr_owner()&nbsp;<wbr>fails for the Ustr. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_setf_share() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function sets the shared mode, which can be observed via. the ustr_shared()&nbsp;<wbr>function. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This is used on a Ustr so that it can have more references than it is able to hold in it&#8217;s reference count. After this call the Ustr can be referenced and unreferenced an infinite number of times. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>After this call the Ustr will never be deleted until ustr_setf_owner()&nbsp;<wbr>is called. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function fails if ustr_alloc()&nbsp;<wbr>fails for the Ustr. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_setf_owner() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function removes the shared mode, which can be observed via. the ustr_shared()&nbsp;<wbr>function. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This is used so that a Ustr in shared mode can be free&#8217;d. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function fails if ustr_alloc()&nbsp;<wbr>fails for the Ustr. </p>
<h2>Comparing data in a Ustr</h2>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_buf() <br/>
 Returns: Less then zero, zero or greater than zero depending on comparison <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to constant bytes, to compare <br/>
 Type <code>[2]</code>: const void * </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of comparison bytes <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like memcmp()&nbsp;<wbr>on the Ustr and the passed data. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp() <br/>
 Returns: Less then zero, zero or greater than zero depending on comparison <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cmp_buf()&nbsp;<wbr>but with the data from ustr_cstr()&nbsp;<wbr>and the length from ustr_len(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_subustr() <br/>
 Returns: Less then zero, zero or greater than zero depending on comparison <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[3]</code>: Position in the Ustr <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: Length to compare from the Ustr <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cmp()&nbsp;<wbr>but with a limit on the data and length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_cstr() <br/>
 Returns: Less then zero, zero or greater than zero depending on comparison <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant C-style string <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cmp_buf()&nbsp;<wbr>but with a length from strlen(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_fast_buf() <br/>
 Returns: Less then zero, zero or greater than zero depending on comparison <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to constant bytes, to compare <br/>
 Type <code>[2]</code>: const void * </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of comparison bytes <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cmp_buf()&nbsp;<wbr>but the order of comparison is optimized for speed, but is much less friendly to humans. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_fast() <br/>
 Returns: Less then zero, zero or greater than zero depending on comparison <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cmp_fast_buf()&nbsp;<wbr>but with the data from ustr_cstr()&nbsp;<wbr>and the length from ustr_len(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_fast_subustr() <br/>
 Returns: Less then zero, zero or greater than zero depending on comparison <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[3]</code>: Position in the Ustr <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: Length to compare from the Ustr <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cmp_fast()&nbsp;<wbr>but with a limit on the data and length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_fast_cstr() <br/>
 Returns: Less then zero, zero or greater than zero depending on comparison <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant C-style string <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cmp_fast_buf()&nbsp;<wbr>but with a length from strlen(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_case_buf() <br/>
 Returns: Less then zero, zero or greater than zero depending on comparison <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to constant bytes, to compare <br/>
 Type <code>[2]</code>: const void * </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of comparison bytes <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cmp_buf()&nbsp;<wbr>but the order of comparison ignores ASCII case. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_case() <br/>
 Returns: Less then zero, zero or greater than zero depending on comparison <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cmp_case_buf()&nbsp;<wbr>but with the data from ustr_cstr()&nbsp;<wbr>and the length from ustr_len(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_case_subustr() <br/>
 Returns: Less then zero, zero or greater than zero depending on comparison <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[3]</code>: Position in the Ustr <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: Length to compare from the Ustr <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cmp_case()&nbsp;<wbr>but with a limit on the data and length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_case_cstr() <br/>
 Returns: Less then zero, zero or greater than zero depending on comparison <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant C-style string <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cmp_case_buf()&nbsp;<wbr>but with a length from strlen(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_eq() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like comparing ustr_cmp()&nbsp;<wbr>against 0. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_buf_eq() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to constant bytes, to compare <br/>
 Type <code>[2]</code>: const void * </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of comparison bytes <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like comparing ustr_cmp_buf()&nbsp;<wbr>against 0. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_subustr_eq() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[3]</code>: Position in the Ustr <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: Length to compare from the Ustr <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like comparing ustr_cmp_subustr()&nbsp;<wbr>against 0. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_cstr_eq() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant C-style string <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like comparing ustr_cmp_cstr()&nbsp;<wbr>against 0. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_case_eq() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like comparing ustr_cmp_case()&nbsp;<wbr>against 0. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_case_buf_eq() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to constant bytes, to compare <br/>
 Type <code>[2]</code>: const void * </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of comparison bytes <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like comparing ustr_cmp_case_buf()&nbsp;<wbr>against 0. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_case_subustr_eq() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[3]</code>: Position in the Ustr <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: Length to compare from the Ustr <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like comparing ustr_cmp_case_subustr()&nbsp;<wbr>against 0. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_case_cstr_eq() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant C-style string <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like comparing ustr_cmp_case_cstr()&nbsp;<wbr>against 0. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_prefix_eq() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like comparing ustr_cmp()&nbsp;<wbr>against 0, but the comparison is limited to the length of the right hand side. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_prefix_buf_eq() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to constant bytes, to compare <br/>
 Type <code>[2]</code>: const void * </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of comparison bytes <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like comparing ustr_cmp_buf()&nbsp;<wbr>against 0, but the comparison is limited to the length of the right hand side&nbsp;<wbr>(Parameter[3]). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_prefix_cstr_eq() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant C-style string <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like comparing ustr_cmp_cstr()&nbsp;<wbr>against 0, but the comparison is limited to the length of the right hand side. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_prefix_subustr_eq() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[3]</code>: Position in the Ustr <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: Length to compare from the Ustr <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like comparing ustr_cmp_subustr()&nbsp;<wbr>against 0, but the comparison is limited to the given length&nbsp;<wbr>(Parameter[4]). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_case_prefix_eq() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like comparing ustr_cmp_case()&nbsp;<wbr>against 0, but the comparison is limited to the length of the right hand side. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_case_prefix_buf_eq() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to constant bytes, to compare <br/>
 Type <code>[2]</code>: const void * </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of comparison bytes <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like comparing ustr_cmp_case_buf()&nbsp;<wbr>against 0, but the comparison is limited to the length of the right hand side&nbsp;<wbr>(Parameter[3]). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_case_prefix_cstr_eq() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant C-style string <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like comparing ustr_cmp_case_cstr()&nbsp;<wbr>against 0, but the comparison is limited to the length of the right hand side. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_case_prefix_subustr_eq() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[3]</code>: Position in the Ustr <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: Length to compare from the Ustr <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like comparing ustr_cmp_case_subustr()&nbsp;<wbr>against 0, but the comparison is limited to the given length&nbsp;<wbr>(Parameter[4]). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_suffix_eq() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cmp_prefix_eq()&nbsp;<wbr>but compares the end of the left hand side. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_suffix_buf_eq() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to constant bytes, to compare <br/>
 Type <code>[2]</code>: const void * </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of comparison bytes <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cmp_prefix_buf_eq()&nbsp;<wbr>but compares the end of the left hand side. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_suffix_cstr_eq() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant C-style string <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cmp_prefix_cstr_eq()&nbsp;<wbr>but compares the end of the left hand side. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_suffix_subustr_eq() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[3]</code>: Position in the Ustr <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: Length to compare from the Ustr <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like comparing ustr_cmp_subustr()&nbsp;<wbr>against 0, but compares the end of the left hand side. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_case_suffix_eq() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cmp_case_prefix_eq()&nbsp;<wbr>but compares the end of the left hand side. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_case_suffix_buf_eq() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to constant bytes, to compare <br/>
 Type <code>[2]</code>: const void * </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of comparison bytes <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cmp_case_prefix_buf_eq()&nbsp;<wbr>but compares the end of the left hand side. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_case_suffix_cstr_eq() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant C-style string <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cmp_case_prefix_cstr_eq()&nbsp;<wbr>but compares the end of the left hand side. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cmp_case_suffix_subustr_eq() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[3]</code>: Position in the Ustr <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: Length to compare from the Ustr <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like comparing ustr_cmp_case_subustr()&nbsp;<wbr>against 0, but compares the end of the left hand side. </p>
<h2>Searching for data in a Ustr</h2>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_srch_chr_fwd() <br/>
 Returns: Position in the Ustr, or zero if not found <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start searching at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Byte data to search for <br/>
 Type <code>[3]</code>: char </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function searches for the data&nbsp;<wbr>(Parameter[3])&nbsp;<wbr>in the Ustr, skipping an offset&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>number of bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_srch_chr_rev() <br/>
 Returns: Position in the Ustr, or zero if not found <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start searching at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Byte data to search for <br/>
 Type <code>[3]</code>: char </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_srch_chr_fwd()&nbsp;<wbr>but it searches from the end of the string to the beginning. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>The searching starts from the end of the string, and so the offset is the offset from the end. However the position of a byte is always relative to the begining, so to do a loop you need to take the position from the length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_srch_buf_fwd() <br/>
 Returns: Position in the Ustr, or zero if not found <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start searching at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to data to search for <br/>
 Type <code>[3]</code>: const void * </p>
<p> <br/>
 Parameter <code>[4]</code>: Length of the data to search for <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function searches for the data&nbsp;<wbr>(Parameter[3])&nbsp;<wbr>of length&nbsp;<wbr>(Parameter[4])&nbsp;<wbr>in the Ustr, skipping an offset&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>number of bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_srch_buf_rev() <br/>
 Returns: Position in the Ustr, or zero if not found <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start searching at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to data to search for <br/>
 Type <code>[3]</code>: const void * </p>
<p> <br/>
 Parameter <code>[4]</code>: Length of the data to search for <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_srch_buf_fwd()&nbsp;<wbr>but it searches from the end of the string to the beginning. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>The searching starts from the end of the string, and so the offset is the offset from the end. However the position of a byte is always relative to the begining, so to do a loop you need to take the position from the length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_srch_fwd() <br/>
 Returns: Position in the Ustr, or zero if not found <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start searching at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant Ustr string, to search for <br/>
 Type <code>[3]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_srch_buf_fwd()&nbsp;<wbr>but it gets the data pointer by calling ustr_cstr()&nbsp;<wbr>and the length by calling ustr_len()&nbsp;<wbr>on the passed Ustr&nbsp;<wbr>(Parameter[3]). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_srch_rev() <br/>
 Returns: Position in the Ustr, or zero if not found <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start searching at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant Ustr string, to search for <br/>
 Type <code>[3]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_srch_fwd()&nbsp;<wbr>but it searches from the end of the string to the beginning. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>The searching starts from the end of the string, and so the offset is the offset from the end. However the position of a byte is always relative to the begining, so to do a loop you need to take the position from the length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_srch_cstr_fwd() <br/>
 Returns: Position in the Ustr, or zero if not found <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start searching at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to C-style string data, to search for <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_srch_buf_fwd()&nbsp;<wbr>but it gets the length by calling strlen()&nbsp;<wbr>on the passed data&nbsp;<wbr>(Parameter[3]). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_srch_cstr_rev() <br/>
 Returns: Position in the Ustr, or zero if not found <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start searching at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to C-style string data, to search for <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_srch_cstr_fwd()&nbsp;<wbr>but it searches from the end of the string to the beginning. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>The searching starts from the end of the string, and so the offset is the offset from the end. However the position of a byte is always relative to the begining, so to do a loop you need to take the position from the length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_srch_subustr_fwd() <br/>
 Returns: Position in the Ustr, or zero if not found <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start searching at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[3]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[4]</code>: Position in the Ustr <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 Parameter <code>[5]</code>: Length of data to search, from the Ustr <br/>
 Type <code>[5]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_srch_fwd()&nbsp;<wbr>but it moves the data to start at the correct position and limits the length to the value specified. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_srch_subustr_rev() <br/>
 Returns: Position in the Ustr, or zero if not found <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start searching at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[3]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[4]</code>: Position in the Ustr <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 Parameter <code>[5]</code>: Length of data to search, from the Ustr <br/>
 Type <code>[5]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_srch_rev()&nbsp;<wbr>but it moves the data to start at the correct position and limits the length to the value specified. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>The searching starts from the end of the string, and so the offset is the offset from the end. However the position of a byte is always relative to the begining, so to do a loop you need to take the position from the length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_srch_case_chr_fwd() <br/>
 Returns: Position in the Ustr, or zero if not found <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start searching at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Byte data to search for <br/>
 Type <code>[3]</code>: char </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_srch_chr_fwd(), but treats ASCII uppercase and lowercase as equivalent. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_srch_case_chr_rev() <br/>
 Returns: Position in the Ustr, or zero if not found <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start searching at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Byte data to search for <br/>
 Type <code>[3]</code>: char </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_srch_chr_fwd(), but treats ASCII uppercase and lowercase as equivalent. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_srch_case_buf_fwd() <br/>
 Returns: Position in the Ustr, or zero if not found <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start searching at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to data to search for <br/>
 Type <code>[3]</code>: const void * </p>
<p> <br/>
 Parameter <code>[4]</code>: Length of the data to search for <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_srch_buf_fwd(), but treats ASCII uppercase and lowercase as equivalent. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_srch_case_buf_rev() <br/>
 Returns: Position in the Ustr, or zero if not found <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start searching at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to data to search for <br/>
 Type <code>[3]</code>: const void * </p>
<p> <br/>
 Parameter <code>[4]</code>: Length of the data to search for <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_srch_buf_rev(), but treats ASCII uppercase and lowercase as equivalent. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_srch_case_fwd() <br/>
 Returns: Position in the Ustr, or zero if not found <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start searching at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant Ustr string, to search for <br/>
 Type <code>[3]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_srch_fwd(), but treats ASCII uppercase and lowercase as equivalent. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_srch_case_rev() <br/>
 Returns: Position in the Ustr, or zero if not found <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start searching at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant Ustr string, to search for <br/>
 Type <code>[3]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_srch_rev(), but treats ASCII uppercase and lowercase as equivalent. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_srch_case_cstr_fwd() <br/>
 Returns: Position in the Ustr, or zero if not found <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start searching at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to C-style string data, to search for <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_srch_cstr_fwd(), but treats ASCII uppercase and lowercase as equivalent. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_srch_case_cstr_rev() <br/>
 Returns: Position in the Ustr, or zero if not found <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start searching at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to C-style string data, to search for <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_srch_cstr_rev(), but treats ASCII uppercase and lowercase as equivalent. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_srch_case_subustr_fwd() <br/>
 Returns: Position in the Ustr, or zero if not found <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start searching at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[3]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[4]</code>: Position in the Ustr <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 Parameter <code>[5]</code>: Length of data to search, from the Ustr <br/>
 Type <code>[5]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_srch_subustr_fwd(), but treats ASCII uppercase and lowercase as equivalent. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_srch_case_subustr_rev() <br/>
 Returns: Position in the Ustr, or zero if not found <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start searching at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[3]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[4]</code>: Position in the Ustr <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 Parameter <code>[5]</code>: Length of data to search, from the Ustr <br/>
 Type <code>[5]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_srch_subustr_rev(), but treats ASCII uppercase and lowercase as equivalent. </p>
<h2>Span lengths of data in a Ustr</h2>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_spn_chr_fwd() <br/>
 Returns: Number of bytes in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, to start spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Byte data <br/>
 Type <code>[3]</code>: char </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function returns the length of the start of the Ustr&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>that only contains bytes that are equal to the data&nbsp;<wbr>(Parameter[3]), skipping offset&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_spn_chr_rev() <br/>
 Returns: Number of bytes in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, to start spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Byte data <br/>
 Type <code>[3]</code>: char </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function returns the length of the end of the Ustr&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>that only contains bytes that are equal to the data&nbsp;<wbr>(Parameter[3]), skipping offset&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_spn_chrs_fwd() <br/>
 Returns: Number of bytes in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, to start spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Array of byte data, for spanning <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 Parameter <code>[4]</code>: Length of byte data, for spanning <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function returns the length of the start of the Ustr&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>that only contains bytes that are equal to any byte in the data&nbsp;<wbr>(Parameter[3]), skipping offset&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_spn_chrs_rev() <br/>
 Returns: Number of bytes in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, to start spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Array of byte data <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 Parameter <code>[4]</code>: Length of byte data <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function returns the length of the end of the Ustr&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>that only contains bytes that are equal to any byte in the data&nbsp;<wbr>(Parameter[3]), skipping offset&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_spn_fwd() <br/>
 Returns: Number of bytes in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, to start spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant Ustr string, containing spanning bytes <br/>
 Type <code>[3]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_spn_buf_fwd()&nbsp;<wbr>but passing ustr_cstr()&nbsp;<wbr>and ustr_len() </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_spn_rev() <br/>
 Returns: Number of bytes in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, to start spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant Ustr string, containing spanning bytes <br/>
 Type <code>[3]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_spn_buf_rev()&nbsp;<wbr>but passing ustr_cstr()&nbsp;<wbr>and ustr_len() </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_spn_cstr_fwd() <br/>
 Returns: Number of bytes in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, to start spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant C-style string, containing spanning bytes <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_spn_buf_fwd()&nbsp;<wbr>but passing strlen()&nbsp;<wbr>for the length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_spn_cstr_rev() <br/>
 Returns: Number of bytes in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, to start spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant C-style string, containing spanning bytes <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_spn_buf_rev()&nbsp;<wbr>but passing strlen()&nbsp;<wbr>for the length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cspn_chr_fwd() <br/>
 Returns: Number of bytes not in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, to start compliment spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Byte data <br/>
 Type <code>[3]</code>: char </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function returns the length of the start of the Ustr&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>that only contains bytes that are not equal to the data&nbsp;<wbr>(Parameter[3]), skipping offset&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cspn_chr_rev() <br/>
 Returns: Number of bytes not in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, to start compliment spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Byte data <br/>
 Type <code>[3]</code>: char </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function returns the length of the end of the Ustr&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>that only contains bytes that are not equal to the data&nbsp;<wbr>(Parameter[3]), skipping offset&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cspn_chrs_fwd() <br/>
 Returns: Number of bytes not in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, to start compliment spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Array of byte data <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 Parameter <code>[4]</code>: Length of byte data <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function returns the length of the start of the Ustr&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>that only contains bytes that are not equal to any byte in the data&nbsp;<wbr>(Parameter[3]), skipping offset&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cspn_chrs_rev() <br/>
 Returns: Number of bytes not in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, to start compliment spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Array of byte data <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 Parameter <code>[4]</code>: Length of byte data <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function returns the length of the end of the Ustr&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>that only contains bytes that are not equal to any byte in the data&nbsp;<wbr>(Parameter[3]), skipping offset&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cspn_fwd() <br/>
 Returns: Number of bytes not in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, to start compliment spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant Ustr string, containing spanning bytes <br/>
 Type <code>[3]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cspn_buf_fwd()&nbsp;<wbr>but passing ustr_cstr()&nbsp;<wbr>and ustr_len() </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cspn_rev() <br/>
 Returns: Number of bytes not in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, to start compliment spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant Ustr string, containing spanning bytes <br/>
 Type <code>[3]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cspn_buf_rev()&nbsp;<wbr>but passing ustr_cstr()&nbsp;<wbr>and ustr_len() </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cspn_cstr_fwd() <br/>
 Returns: Number of bytes not in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, to start compliment spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant C-style string, containing spanning bytes <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cspn_buf_fwd()&nbsp;<wbr>but passing strlen()&nbsp;<wbr>for the length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cspn_cstr_rev() <br/>
 Returns: Number of bytes not in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, to start spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant C-style string, containing spanning bytes <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cspn_buf_rev()&nbsp;<wbr>but passing strlen()&nbsp;<wbr>for the length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_utf8_spn_chrs_fwd() <br/>
 Returns: Number of UTF-8 characters not in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr UTF-8 string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, in UTF-8 characters, to start spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant C-style UTF-8 string <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 Parameter <code>[4]</code>: Length of the C-style UTF-8 string <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_spn_chrs_fwd()&nbsp;<wbr>but the return value, offset, and length all use UTF-8 characters and not bytes. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This is much slower than ustr_spn_chrs_fwd()&nbsp;<wbr>but given&nbsp;<wbr>&quot;xy&quot;&nbsp;<wbr>as a multi-byte UTF-8 character it understands that the span over&nbsp;<wbr>&quot;xyxz&quot;&nbsp;<wbr>is 1 UTF-8 character and not 3 bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_utf8_spn_chrs_rev() <br/>
 Returns: Number of UTF-8 characters not in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr UTF-8 string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, in UTF-8 characters, to start spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant C-style UTF-8 string <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 Parameter <code>[4]</code>: <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_spn_chrs_rev()&nbsp;<wbr>but the return value, offset, and length all use UTF-8 characters and not bytes. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This is much slower than ustr_spn_chrs_rev()&nbsp;<wbr>but given&nbsp;<wbr>&quot;xy&quot;&nbsp;<wbr>as a multi-byte UTF-8 character it understands that the span over&nbsp;<wbr>&quot;xyxz&quot;&nbsp;<wbr>is 1 UTF-8 character and not 3 bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_utf8_spn_fwd() <br/>
 Returns: Number of UTF-8 characters not in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr UTF-8 string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, in UTF-8 characters, to start spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant Ustr UTF-8 string <br/>
 Type <code>[3]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_spn_fwd()&nbsp;<wbr>but the return value, offset, and length all use UTF-8 characters and not bytes. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This is much slower than ustr_spn_fwd()&nbsp;<wbr>but given&nbsp;<wbr>&quot;xy&quot;&nbsp;<wbr>as a multi-byte UTF-8 character it understands that the span over&nbsp;<wbr>&quot;xyxz&quot;&nbsp;<wbr>is 1 UTF-8 character and not 3 bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_utf8_spn_rev() <br/>
 Returns: Number of UTF-8 characters not in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr UTF-8 string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, in UTF-8 characters, to start spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant Ustr UTF-8 string <br/>
 Type <code>[3]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_spn_rev()&nbsp;<wbr>but the return value, offset, and length all use UTF-8 characters and not bytes. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This is much slower than ustr_spn_rev()&nbsp;<wbr>but given&nbsp;<wbr>&quot;xy&quot;&nbsp;<wbr>as a multi-byte UTF-8 character it understands that the span over&nbsp;<wbr>&quot;xyxz&quot;&nbsp;<wbr>is 1 UTF-8 character and not 3 bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_utf8_spn_cstr_fwd() <br/>
 Returns: Number of UTF-8 characters not in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr UTF-8 string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, in UTF-8 characters, to start spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant C-style UTF-8 string <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_spn_cstr_fwd()&nbsp;<wbr>but the return value, offset, and length all use UTF-8 characters and not bytes. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This is much slower than ustr_spn_cstr_fwd()&nbsp;<wbr>but given&nbsp;<wbr>&quot;xy&quot;&nbsp;<wbr>as a multi-byte UTF-8 character it understands that the span over&nbsp;<wbr>&quot;xyxz&quot;&nbsp;<wbr>is 1 UTF-8 character and not 3 bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_utf8_spn_cstr_rev() <br/>
 Returns: Number of UTF-8 characters not in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr UTF-8 string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, in UTF-8 characters, to start spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant C-style UTF-8 string <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_spn_cstr_rev()&nbsp;<wbr>but the return value, offset, and length all use UTF-8 characters and not bytes. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This is much slower than ustr_spn_cstr_rev()&nbsp;<wbr>but given&nbsp;<wbr>&quot;xy&quot;&nbsp;<wbr>as a multi-byte UTF-8 character it understands that the span over&nbsp;<wbr>&quot;xyxz&quot;&nbsp;<wbr>is 1 UTF-8 character and not 3 bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_utf8_cspn_chrs_fwd() <br/>
 Returns: Number of UTF-8 characters not in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr UTF-8 string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, in UTF-8 characters, to start compliment spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant C-style UTF-8 string <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 Parameter <code>[4]</code>: Length of the C-style UTF-8 string <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cspn_chrs_fwd()&nbsp;<wbr>but the return value, offset, and length all use UTF-8 characters and not bytes. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This is much slower than ustr_cspn_chrs_fwd()&nbsp;<wbr>but given&nbsp;<wbr>&quot;xy&quot;&nbsp;<wbr>as a multi-byte UTF-8 character it understands that the compliment span over&nbsp;<wbr>&quot;xzxy&quot;&nbsp;<wbr>is 1 UTF-8 character and not 0 bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_utf8_cspn_chrs_rev() <br/>
 Returns: Number of UTF-8 characters not in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr UTF-8 string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, in UTF-8 characters, to start compliment spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant C-style UTF-8 string <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 Parameter <code>[4]</code>: Length of the C-style UTF-8 string <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cspn_chrs_rev()&nbsp;<wbr>but the return value, offset, and length all use UTF-8 characters and not bytes. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This is much slower than ustr_cspn_chrs_rev()&nbsp;<wbr>but given&nbsp;<wbr>&quot;xy&quot;&nbsp;<wbr>as a multi-byte UTF-8 character it understands that the compliment span over&nbsp;<wbr>&quot;xzxy&quot;&nbsp;<wbr>is 1 UTF-8 character and not 0 bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_utf8_cspn_fwd() <br/>
 Returns: Number of UTF-8 characters not in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr UTF-8 string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, in UTF-8 characters, to start compliment spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant Ustr UTF-8 string, containing spanning data <br/>
 Type <code>[3]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cspn_fwd()&nbsp;<wbr>but the return value, offset, and length all use UTF-8 characters and not bytes. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This is much slower than ustr_cspn_fwd()&nbsp;<wbr>but given&nbsp;<wbr>&quot;xy&quot;&nbsp;<wbr>as a multi-byte UTF-8 character it understands that the compliment span over&nbsp;<wbr>&quot;xzxy&quot;&nbsp;<wbr>is 1 UTF-8 character and not 0 bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_utf8_cspn_rev() <br/>
 Returns: Number of UTF-8 characters not in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr UTF-8 string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, in UTF-8 characters, to start compliment spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to constant Ustr UTF-8 string data, containing spanning data <br/>
 Type <code>[3]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cspn_rev()&nbsp;<wbr>but the return value, offset, and length all use UTF-8 characters and not bytes. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This is much slower than ustr_cspn_rev()&nbsp;<wbr>but given&nbsp;<wbr>&quot;xy&quot;&nbsp;<wbr>as a multi-byte UTF-8 character it understands that the compliment span over&nbsp;<wbr>&quot;xzxy&quot;&nbsp;<wbr>is 1 UTF-8 character and not 0 bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_utf8_cspn_cstr_fwd() <br/>
 Returns: Number of UTF-8 characters not in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr UTF-8 string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, in UTF-8 characters, to start compliment spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to constant C-style UTF-8 string data, containing spanning data <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cspn_cstr_fwd()&nbsp;<wbr>but the return value, offset, and length all use UTF-8 characters and not bytes. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This is much slower than ustr_cspn_cstr_fwd()&nbsp;<wbr>but given&nbsp;<wbr>&quot;xy&quot;&nbsp;<wbr>as a multi-byte UTF-8 character it understands that the compliment span over&nbsp;<wbr>&quot;xzxy&quot;&nbsp;<wbr>is 1 UTF-8 character and not 0 bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_utf8_cspn_cstr_rev() <br/>
 Returns: Number of UTF-8 characters not in the span <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr UTF-8 string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string, in UTF-8 characters, to start compliment spanning from <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to C-style UTF-8 string data, containing spanning data <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_cspn_cstr_rev()&nbsp;<wbr>but the return value, offset, and length all use UTF-8 characters and not bytes. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This is much slower than ustr_spn_cstr_rev()&nbsp;<wbr>but given&nbsp;<wbr>&quot;xy&quot;&nbsp;<wbr>as a multi-byte UTF-8 character it understands that the compliment span over&nbsp;<wbr>&quot;xzxy&quot;&nbsp;<wbr>is 1 UTF-8 character and not 0 bytes. </p>
<h2>Doing IO from or to a Ustr</h2>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_io_get() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a C file object <br/>
 Type <code>[2]</code>: FILE * </p>
<p> <br/>
 Parameter <code>[3]</code>: Number of bytes to read <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: Returned number of bytes read <br/>
 Type <code>[4]</code>: size_t * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function tries to read a minimum number of bytes from the file object, into the Ustr string. The exact number read is returned, unless&nbsp;<wbr>(Parameter[4])&nbsp;<wbr>is NULL. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_io_getfile() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a C file object <br/>
 Type <code>[2]</code>: FILE * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function calls ustr_io_get()&nbsp;<wbr>rpeatedly until EOF is encountered. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>The errno value when this function ends could either be from fopen(), fread(), or if both of the those succeeded from fclose(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_io_getfilename() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A C-style string of a filename <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function opens a specified file, and then calls ustr_io_getfile(). Finally closing the FILE&nbsp;<wbr>*&nbsp;<wbr>object. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_io_getdelim() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a C file object <br/>
 Type <code>[2]</code>: FILE * </p>
<p> <br/>
 Parameter <code>[3]</code>: A delimiter byte to stop reading at <br/>
 Type <code>[3]</code>: char </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function reads bytes from the file until it hits the delimiter byte. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>The delimiter is included, use ustr_del()&nbsp;<wbr>to remove 1 byte from the end if you don&#8217;t want it. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function assumes a delimiter will happen every 80 bytes or so. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_io_getline() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a C file object <br/>
 Type <code>[2]</code>: FILE * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling ustr_io_getdelim()&nbsp;<wbr>with&nbsp;<wbr>&#8216;\n&#8217;&nbsp;<wbr>as the delimiter. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_io_put() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a C file object <br/>
 Type <code>[2]</code>: FILE * </p>
<p> <br/>
 Parameter <code>[3]</code>: Number of bytes to write <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function is the opposite of ustr_io_get(), taking bytes from the beginning of the Ustr and writting them to the file. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>Deleting bytes from the begining of a Ustr string is the most inefficient thing to do, so it is recommended to use ustr_io_putfile(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_io_putline() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a C file object <br/>
 Type <code>[2]</code>: FILE * </p>
<p> <br/>
 Parameter <code>[3]</code>: Number of bytes to write <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling ustr_io_put(), and then writting a&nbsp;<wbr>&#8216;\n&#8217;&nbsp;<wbr>to the file. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This doesn&#8217;t write a line from the Ustr to the file, if you want that call ustr_io_put()&nbsp;<wbr>directly, using the return from ustr_srch_chr_fwd()&nbsp;<wbr>(with a&nbsp;<wbr>&#8216;\n&#8217;)&nbsp;<wbr>as the number of bytes argument. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_io_putfile() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a C file object <br/>
 Type <code>[2]</code>: FILE * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling ustr_io_put()&nbsp;<wbr>with ustr_len()&nbsp;<wbr>as the number of bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_io_putfileline() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a C file object <br/>
 Type <code>[2]</code>: FILE * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling ustr_io_putline()&nbsp;<wbr>with ustr_len()&nbsp;<wbr>as the number of bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_io_putfilename() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A C-style string of a filename <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 Parameter <code>[3]</code>: A C-style string of a filemode (the second argument to fopen) <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function opens a specified file, and then calls ustr_io_putfile(). Finally closing the FILE&nbsp;<wbr>*&nbsp;<wbr>object. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>The errno value when this function ends could either be from fopen(), fwrite(), or if both of the those succeeded from fclose(). </p>
<h2>String substitution/replacement</h2>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sub_undef() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position where to start substitution <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of undefined data <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>The Ustr string is expanded as required&nbsp;<wbr>(possibly reallocated)&nbsp;<wbr>so that it can contain length&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>data, from the required position. If the length is not zero the Ustr will be writable. Or it&#8217;ll return USTR_FALSE&nbsp;<wbr>(zero)&nbsp;<wbr>on failure. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>You can think of the operation as two seperate tasks, one which makes the current data in the Ustr undefined and the second which adds undefined data to the ustr to accomodate the desired length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sub_buf() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position where to start substitution <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Buffer containing substitution string <br/>
 Type <code>[3]</code>: const void * </p>
<p> <br/>
 Parameter <code>[4]</code>: Length of buffer <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_sub_undef()&nbsp;<wbr>and then copied the data into the new undefined space. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sub_cstr() <br/>
 Returns: success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position where to start substitution <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant C-style string, which is the substitution <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_sub_buf()&nbsp;<wbr>but the length is worked out automatically by strlen(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR_SUB_OSTR() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position where to start substitution <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A constant C-style string <br/>
 Type <code>[3]</code>: const char [] </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_sub_buf()&nbsp;<wbr>and passed sizeof()&nbsp;<wbr>- 1 as the length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR_SUB_OBJ() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position where to start substitution <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A symbol <br/>
 Type <code>[3]</code>: ... </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_sub_buf()&nbsp;<wbr>and passed sizeof()&nbsp;<wbr>as the length. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>In most cases you&#8217;ll want to use USTR_SUB_OSTR(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sub() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position where to start substitution <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[3]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_sub_buf()&nbsp;<wbr>with the ustr_cstr()&nbsp;<wbr>and ustr_len()&nbsp;<wbr>values of the Ustr string to be added. The exception being if you substitute a ustr into itself, while only having a single reference count, the simple method could access a free&#8217;d ustr data, but this function just works. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sub_subustr() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position where to start substitution <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[3]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[4]</code>: Position in the Ustr <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 Parameter <code>[5]</code>: Length to substitute from the Ustr <br/>
 Type <code>[5]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function mostly as if you had called ustr_sub_buf()&nbsp;<wbr>with the ustr_cstr()&nbsp;<wbr>+&nbsp;<wbr>position - 1 and length values of the Ustr string to be insed. The exception being if you insert a ustr to itself, while only having a single reference count, the simple method would access a free&#8217;d ustr data, but this function just works. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_sub_undef() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position where to start substitution <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of substitution <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: Length of undefined data <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had done ustr_del_subustr()&nbsp;<wbr>followed by ustr_ins_undef(), however it is significantly more efficient. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_sub_buf() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position where to start substitution <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of substitution <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: Buffer containting substitute data <br/>
 Type <code>[4]</code>: const void * </p>
<p> <br/>
 Parameter <code>[5]</code>: Length of Buffer <br/>
 Type <code>[5]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function will substitute a specific number of characters in a Ustr with the data from a buffer, this function does the job of one or more of ustr_add_buf(), ustr_sub_buf()&nbsp;<wbr>and ustr_del(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_sub_cstr() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position where to start replacement <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of substitution <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: A pointer to a constant C-style string, containing spanning bytes <br/>
 Type <code>[4]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_sc_sub_buf()&nbsp;<wbr>but the length is worked out automatically by strlen(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_sub() <br/>
 Returns: success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position where to start substitution <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of substitution <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: Pointer to a Ustr containing the substitute string <br/>
 Type <code>[4]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_sc_sub_buf()&nbsp;<wbr>with the ustr_cstr()&nbsp;<wbr>and ustr_len()&nbsp;<wbr>values of the Ustr string to be added. The exception being if you substitute a ustr into itself, while only having a single reference count, the simple method could access a free&#8217;d ustr data, but this function just works. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_sub_subustr() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position where to start substitution <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of substitution <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[4]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[5]</code>: Position in the Ustr <br/>
 Type <code>[5]</code>: size_t </p>
<p> <br/>
 Parameter <code>[6]</code>: Length to substitute from the Ustr <br/>
 Type <code>[6]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function mostly as if you had called ustr_sc_sub_buf()&nbsp;<wbr>with the ustr_cstr()&nbsp;<wbr>+&nbsp;<wbr>position - 1 and length values of the Ustr string to be insed. The exception being if you insert a ustr to itself, while only having a single reference count, the simple method would access a free&#8217;d ustr data, but this function just works. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR_SC_SUB_OSTR() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position where to start substitution <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of substitution <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: A constant C-style string <br/>
 Type <code>[4]</code>: const char [] </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_sc_sub_buf()&nbsp;<wbr>and passed sizeof()&nbsp;<wbr>- 1 as the length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> USTR_SC_SUB_OBJ() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Position where to start substitution <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of substitution <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: A symbol <br/>
 Type <code>[4]</code>: ... </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_sc_sub_buf()&nbsp;<wbr>and passed sizeof()&nbsp;<wbr>as the length. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>In most cases you&#8217;ll want to use USTR_SUB_OSTR(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_replace_buf() <br/>
 Returns: Number of tokens replaced <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr (haystack) <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Buffer containting search data <br/>
 Type <code>[2]</code>: const void * </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of search buffer <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: Buffer containting replacement data <br/>
 Type <code>[4]</code>: const void * </p>
<p> <br/>
 Parameter <code>[5]</code>: Length of replacement buffer <br/>
 Type <code>[5]</code>: size_t </p>
<p> <br/>
 Parameter <code>[6]</code>: Maximum number of matches to replace (0 for unlimited) <br/>
 Type <code>[6]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function scans the&nbsp;<wbr>&quot;haystack&quot;&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>for&nbsp;<wbr>&quot;needle&quot;&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>and replaces max_replacements&nbsp;<wbr>(Parameter[6])&nbsp;<wbr>matches with the&nbsp;<wbr>&quot;replacement&quot;&nbsp;<wbr>(Parameter[4]). </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>If max_replacements&nbsp;<wbr>(Parameter[6])&nbsp;<wbr>is 0, this function will replace ALL occurrences. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_replace_cstr() <br/>
 Returns: Number of tokens replaced <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr (haystack) <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant C-style string, containing search bytes <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 Parameter <code>[3]</code>: A pointer to a constant C-style string, containing replacement bytes <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 Parameter <code>[4]</code>: Maximum number of matches to replace (0 for unlimited) <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_replace_buf()&nbsp;<wbr>but gets the lengths for the buffer automatically from strlen(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_replace() <br/>
 Returns: Number of tokens replaced <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr (haystack) <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Ustr to search for (needle) <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[3]</code>: Ustr to replace needle with <br/>
 Type <code>[3]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[4]</code>: Maximum number of matches to replace (0 for unlimited) <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_replace_buf()&nbsp;<wbr>but gets the lengths from the ustr automatically. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_replace_rep_chr() <br/>
 Returns: number of replacements made <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: pointer to a pointer to a Ustr to be modified <br/>
 Type <code>[1]</code>: struct Ustr **ps1 </p>
<p> <br/>
 Parameter <code>[2]</code>: character to replace <br/>
 Type <code>[2]</code>: char </p>
<p> <br/>
 Parameter <code>[3]</code>: number of characters to replace <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: character to replace with <br/>
 Type <code>[4]</code>: char </p>
<p> <br/>
 Parameter <code>[5]</code>: number of characters to replace with <br/>
 Type <code>[5]</code>: size_t nlen </p>
<p> <br/>
 Parameter <code>[6]</code>: maximum number of replacements to make (use 0 for unlimited) <br/>
 Type <code>[6]</code>: size_t lim </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function replaces a repeating sequence of characters with another repeating sequence of characters.&nbsp;<wbr> <br/>
&nbsp;<wbr>&nbsp;<wbr>For example... </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>Ustr&nbsp;<wbr>*data&nbsp;<wbr>=&nbsp;<wbr>ustr_dup_cstr(&quot;xxxBxxCxDxxx&quot;); <br/>
&nbsp;<wbr>&nbsp;<wbr>ustr_replace_rep_chr(&amp;data,&#8216;x&#8217;,2,&#8216;y&#8217;,1, 0) </p>
<p> <br/>
&nbsp;<wbr>...would change data to be&nbsp;<wbr>&quot;yxByCxDyx&quot;. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>Changing the same letter the same number of times is considered a No-op since it is a vast performance improvement this way. So passing in&nbsp;<wbr>&nbsp;<wbr>(&amp;data,&#8216;y&#8217;,2,&#8216;y&#8217;,2 ,0)&nbsp;<wbr>will have a return value of 0 and the string will be unchanged. </p>
<h2>Splitting a Ustr</h2>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_split_buf() <br/>
 Returns: pointer to a Ustr representing the next token <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a constant Ustr to be split <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Pointer to an offset <br/>
 Type <code>[2]</code>: size_t * </p>
<p> <br/>
 Parameter <code>[3]</code>: Buffer to use as split search pattern <br/>
 Type <code>[3]</code>: const void * </p>
<p> <br/>
 Parameter <code>[4]</code>: Length of buffer <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 Parameter <code>[5]</code>: Pointer to a Ustr to be used as the return value <br/>
 Type <code>[5]</code>: struct Ustr * </p>
<p> <br/>
 Parameter <code>[6]</code>: Flags with the prefix USTR_FLAG_SPLIT_ <br/>
 Type <code>[6]</code>: unsigned int </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works in a manner similar to strtok(). Each time the function is called, the string inside of the buffer&nbsp;<wbr>(Parameter[3])&nbsp;<wbr>is used as a search pattern at which to split. If the pattern is not found, the entire string will be returned. A USTR_NULL return value indicates there are no more tokens remaining. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>Parameter[5]&nbsp;<wbr>is a a pointer to a Ustr where the return value will be placed. Passing a USTR_NULL to this parameter will cause the string to be allocated and&nbsp;<wbr><code>MUST</code>&nbsp;<wbr>be freed&nbsp;<wbr><code>manually</code>. If, however, you pass in a non-null Ustr to this parameter, each call to ustr_split_buf()&nbsp;<wbr>will free what is in this pointer and place the new token there&nbsp;<wbr>(when USTR_NULL is returned, nothing needs to be free&#8217;d).&nbsp;<wbr>&nbsp;<wbr>For example, given... </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>Ustr&nbsp;<wbr>*data&nbsp;<wbr>=&nbsp;<wbr>...; <br/>
&nbsp;<wbr>&nbsp;<wbr>Ustr&nbsp;<wbr>*tok&nbsp;<wbr>=&nbsp;<wbr>USTR_NULL; <br/>
&nbsp;<wbr>&nbsp;<wbr>const char&nbsp;<wbr>*sep&nbsp;<wbr>=&nbsp;<wbr>&quot;,&quot;; <br/>
&nbsp;<wbr>&nbsp;<wbr>size_t off&nbsp;<wbr>=&nbsp;<wbr>0; <br/>
&nbsp;<wbr>&nbsp;<wbr>unsigned int flags&nbsp;<wbr>=&nbsp;<wbr>USTR_FLAGS_SPLIT_DEF; </p>
<p> <br/>
&nbsp;<wbr>...there are two options... </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>while&nbsp;<wbr>((tok&nbsp;<wbr>=&nbsp;<wbr>ustr_split_buf(data,&nbsp;<wbr>&amp;off, sep, strlen(sep), tok, flags))) <br/>
&nbsp;<wbr>&nbsp;<wbr>{ <br/>
&nbsp;<wbr>/*&nbsp;<wbr>Do something with tok -- but next iteration of the loop will free <br/>
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>and overwrite tok, so you must ustr_dup()&nbsp;<wbr>if you want to keep it&nbsp;<wbr>*/ <br/>
&nbsp;<wbr>&nbsp;<wbr>} <br/>
&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>tok is now NULL again after the loop&nbsp;<wbr>*/ </p>
<p> <br/>
&nbsp;<wbr>...or... </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>while&nbsp;<wbr>((tok&nbsp;<wbr>=&nbsp;<wbr>ustr_split_buf(data,&nbsp;<wbr>&amp;off, sep, strlen(sep), USTR_NULL, flags))) <br/>
&nbsp;<wbr>&nbsp;<wbr>{ <br/>
&nbsp;<wbr>/*&nbsp;<wbr>Do something with tok, and it will NOT be freed in the next iteration of <br/>
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>the loop&nbsp;<wbr>*/ <br/>
ustr_free(tok);&nbsp;<wbr>/*&nbsp;<wbr>have to free to avoid mem leaks&nbsp;<wbr>*/ <br/>
&nbsp;<wbr>&nbsp;<wbr>} </p>
<p> <br/>
&nbsp;<wbr>...the former of which being the safer option. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>There are several flags that will alter the behaviour of this function, all of which have a common with the default being USTR_FLAG_SPLIT_DEF. <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>If you are calling this function directly, it is very likely that you&#8217;d want to use ustr_split_cstr()&nbsp;<wbr>instead. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_split() <br/>
 Returns: Pointer to a Ustr representing the next token <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a constant Ustr to be split <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Pointer to an offset variable <br/>
 Type <code>[2]</code>: size_t * </p>
<p> <br/>
 Parameter <code>[3]</code>: Pointer to a constant Ustr to use as the split search pattern <br/>
 Type <code>[3]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[4]</code>: Pointer to a Ustr where the return value will be placed <br/>
 Type <code>[4]</code>: struct Ustr * </p>
<p> <br/>
 Parameter <code>[5]</code>: Flags <br/>
 Type <code>[5]</code>: unsigned int </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
Works like ustr_split_buf()&nbsp;<wbr>but takes a Ustr as the split search pattern <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>instead. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_split_cstr() <br/>
 Returns: Pointer to a Ustr representing the next token <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a constant Ustr to be split <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Pointer to an offset variable <br/>
 Type <code>[2]</code>: size_t * </p>
<p> <br/>
 Parameter <code>[3]</code>: C string to use as split search pattern <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 Parameter <code>[4]</code>: Pointer to a Ustr where the return value will be placed <br/>
 Type <code>[4]</code>: struct Ustr * </p>
<p> <br/>
 Parameter <code>[5]</code>: Flags <br/>
 Type <code>[5]</code>: unsigned int </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>Works like ustr_split_buf()&nbsp;<wbr>but takes a C string as the split search pattern, and so gets the length via. strlen(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_split_spn_chrs() <br/>
 Returns: Pointer to a Ustr representing the next token <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a Ustr to be split <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Pointer to an offset variable <br/>
 Type <code>[2]</code>: size_t * </p>
<p> <br/>
 Parameter <code>[3]</code>: String representing a set of bytes to use as split chars <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 Parameter <code>[4]</code>: Length of the string of set of bytes <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 Parameter <code>[5]</code>: Pointer to a Ustr where the return value will be placed <br/>
 Type <code>[5]</code>: struct Ustr * </p>
<p> <br/>
 Parameter <code>[6]</code>: flags <br/>
 Type <code>[6]</code>: unsigned int </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>Works like ustr_split_buf()&nbsp;<wbr>but uses the individual ASCII bytes in the separator string&nbsp;<wbr>(Parameter[3])&nbsp;<wbr>as search patterns. It will split if&nbsp;<wbr><code>ANY</code>&nbsp;<wbr>of these individual characters are matched&nbsp;<wbr>(much like strtok()). For example: if splitting&nbsp;<wbr>&quot;this, is,a test&quot;&nbsp;<wbr>with the separator string&nbsp;<wbr>&quot;,&nbsp;<wbr>&quot;&nbsp;<wbr>the tokens returned would be&nbsp;<wbr>{&quot;this&quot;&nbsp;<wbr>&quot;is&quot;&nbsp;<wbr>&quot;a&quot;&nbsp;<wbr>&quot;test&quot;}; </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>If you are calling this function directly, it is very likely that you&#8217;d want to use ustr_split_spn_cstr()&nbsp;<wbr>instead. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_split_spn_cstr() <br/>
 Returns: Pointer to a Ustr representing the next token <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a Ustr to be split <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Pointer to an offset variable <br/>
 Type <code>[2]</code>: size_t * </p>
<p> <br/>
 Parameter <code>[3]</code>: String representing a set of bytes to use as split chars <br/>
 Type <code>[3]</code>: const char * </p>
<p> <br/>
 Parameter <code>[4]</code>: Pointer to a Ustr where the return value will be placed <br/>
 Type <code>[4]</code>: struct Ustr * </p>
<p> <br/>
 Parameter <code>[5]</code>: flags <br/>
 Type <code>[5]</code>: unsigned int </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>Works like ustr_split_spn_chrs()&nbsp;<wbr>but gets the length automatically via. strlen(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_split_spn() <br/>
 Returns: Pointer to a Ustr representing the next token <br/>
 Type: struct Ustr * </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a constant Ustr to be split <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Pointer to an offset variable <br/>
 Type <code>[2]</code>: size_t * </p>
<p> <br/>
 Parameter <code>[3]</code>: Pointer to a constant Ustr to use as the split search pattern <br/>
 Type <code>[3]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[4]</code>: Pointer to a Ustr where the return value will be placed <br/>
 Type <code>[4]</code>: struct Ustr * </p>
<p> <br/>
 Parameter <code>[5]</code>: Flags <br/>
 Type <code>[5]</code>: unsigned int </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>Works like ustr_split_spn_chrs()&nbsp;<wbr>but takes a Ustr as the split chars instead. </p>
<h2>Dealing with UTF-8 in a Ustr</h2>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_utf8_valid() <br/>
 Returns: A boolean flag of either USTR_TRUE or USTR_FALSE <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function tries it&#8217;s best to find out if the string is a valid utf-8 string. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_utf8_len() <br/>
 Returns: The number of the utf-8 characters in the Ustr <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function counts the number of utf-8 characters inn the Ustr. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function gives undefined answers on strings that aren&#8217;t utf-8 valid. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_utf8_width() <br/>
 Returns: ssize_t <br/>
 Type: ssize_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function returns the visible width of the string, assuming it is a valid utf-8 string. This is like converting to wide characters and using wcwidth(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_utf8_chars2bytes() <br/>
 Returns: Length of span in bytes <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Position of a span in utf-8 characters <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of a span in utf-8 characters <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: Returns the position of the span in bytes <br/>
 Type <code>[4]</code>: size_t * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function converts a span, in utf-8 characters, to the same span in bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_utf8_bytes2chars() <br/>
 Returns: Returns the position of a span in utf-8 characters <br/>
 Type: size_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Position of a span in bytes <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of a span in bytes <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: Returns length of a span in utf-8 characters <br/>
 Type <code>[4]</code>: size_t * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function converts a span, in bytes, to the same span in utf-8 characters. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>Because a byte span can start or end within a utf-8 character, converting the return values back into bytes via. ustr_utf8_chars2bytes()&nbsp;<wbr>may make the span be slightly bigger&nbsp;<wbr>(position slightly earlier, and the length slightly longer). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_utf8_reverse() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function reverses the utf-8 characters in the Ustr string, assuming it is a valid utf-8 string, so the last one becomes the first and the second to last becomes the second etc. </p>
<h2>Parsing ASCII integer numbers from a Ustr</h2>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_parse_uintmaxx() <br/>
 Returns: Parsed number, or zero on error <br/>
 Type: uintmax_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start parsing at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Base (2-36) and flags, starting with USTR_FLAG_PARSE_NUM_ <br/>
 Type <code>[3]</code>: unsigned int </p>
<p> <br/>
 Parameter <code>[4]</code>: Absolute minimum value <br/>
 Type <code>[4]</code>: uintmax_t </p>
<p> <br/>
 Parameter <code>[5]</code>: Absolute maximum value <br/>
 Type <code>[5]</code>: uintmax_t </p>
<p> <br/>
 Parameter <code>[6]</code>: Thousands separator <br/>
 Type <code>[6]</code>: const char * </p>
<p> <br/>
 Parameter <code>[7]</code>: Return length of parsed number <br/>
 Type <code>[7]</code>: size_t * </p>
<p> <br/>
 Parameter <code>[8]</code>: Return error code, starting with USTR_TYPE_PARSE_NUM_ERR_ <br/>
 Type <code>[8]</code>: unsigned int * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function parses an ASCII representation of a number from a Ustr&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>starting at the offset&nbsp;<wbr>(Parameter[2]). </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>If stdint.h isn&#8217;t available this function won&#8217;t be available. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_parse_uintmax() <br/>
 Returns: Parsed number, or zero on error <br/>
 Type: uintmax_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start parsing at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Base (2-36) and flags, starting with USTR_FLAG_PARSE_NUM_ <br/>
 Type <code>[3]</code>: unsigned int </p>
<p> <br/>
 Parameter <code>[4]</code>: Return length of parsed number <br/>
 Type <code>[4]</code>: size_t * </p>
<p> <br/>
 Parameter <code>[5]</code>: Return error code, starting with USTR_TYPE_PARSE_NUM_ERR_ <br/>
 Type <code>[5]</code>: unsigned int * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_parse_uintmaxx()&nbsp;<wbr>with the minimum and maximum values taken as 0 and UINTMAX_MAX, and the thousands separator as&nbsp;<wbr>&quot;_&quot;. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>If stdint.h isn&#8217;t available this function won&#8217;t be available. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_parse_intmax() <br/>
 Returns: Parsed number, or zero on error <br/>
 Type: intmax_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start parsing at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Base (2-36) and flags, starting with USTR_FLAG_PARSE_NUM_ <br/>
 Type <code>[3]</code>: unsigned int </p>
<p> <br/>
 Parameter <code>[4]</code>: Return length of parsed number <br/>
 Type <code>[4]</code>: size_t * </p>
<p> <br/>
 Parameter <code>[5]</code>: Return error code, starting with USTR_TYPE_PARSE_NUM_ERR_ <br/>
 Type <code>[5]</code>: unsigned int * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_parse_uintmaxx()&nbsp;<wbr>with the minimum and maximum values taken as -INTMAX_MIN and INTMAX_MAX, and the thousands separator as&nbsp;<wbr>&quot;_&quot;. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>If stdint.h isn&#8217;t available this function won&#8217;t be available. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_parse_ulongx() <br/>
 Returns: Parsed number, or zero on error <br/>
 Type: unsigned long </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start parsing at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Base (2-36) and flags, starting with USTR_FLAG_PARSE_NUM_ <br/>
 Type <code>[3]</code>: unsigned int </p>
<p> <br/>
 Parameter <code>[4]</code>: Absolute minimum value <br/>
 Type <code>[4]</code>: unsigned long </p>
<p> <br/>
 Parameter <code>[5]</code>: Absolute maximum value <br/>
 Type <code>[5]</code>: unsigned long </p>
<p> <br/>
 Parameter <code>[6]</code>: Thousands separator <br/>
 Type <code>[6]</code>: const char * </p>
<p> <br/>
 Parameter <code>[7]</code>: Return length of parsed number <br/>
 Type <code>[7]</code>: size_t * </p>
<p> <br/>
 Parameter <code>[8]</code>: Return error code, starting with USTR_TYPE_PARSE_NUM_ERR_ <br/>
 Type <code>[8]</code>: unsigned int * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_parse_uintmaxx()&nbsp;<wbr>but returns an unsigned long, it is always available even when stdint.h isn&#8217;t. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_parse_ulong() <br/>
 Returns: Parsed number, or zero on error <br/>
 Type: unsigned long </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start parsing at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Base (2-36) and flags, starting with USTR_FLAG_PARSE_NUM_ <br/>
 Type <code>[3]</code>: unsigned int </p>
<p> <br/>
 Parameter <code>[4]</code>: Return length of parsed number <br/>
 Type <code>[4]</code>: size_t * </p>
<p> <br/>
 Parameter <code>[5]</code>: Return error code, starting with USTR_TYPE_PARSE_NUM_ERR_ <br/>
 Type <code>[5]</code>: unsigned int * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_parse_ulongx()&nbsp;<wbr>with the minimum and maximum values taken as 0 and ULONG_MAX, and the thousands separator as&nbsp;<wbr>&quot;_&quot;. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_parse_long() <br/>
 Returns: Parsed number, or zero on error <br/>
 Type: long </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start parsing at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Base (2-36) and flags, starting with USTR_FLAG_PARSE_NUM_ <br/>
 Type <code>[3]</code>: unsigned int </p>
<p> <br/>
 Parameter <code>[4]</code>: Return length of parsed number <br/>
 Type <code>[4]</code>: size_t * </p>
<p> <br/>
 Parameter <code>[5]</code>: Return error code, starting with USTR_TYPE_PARSE_NUM_ERR_ <br/>
 Type <code>[5]</code>: unsigned int * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_parse_ulongx()&nbsp;<wbr>with the minimum and maximum values taken as -LONG_MIN and LONG_MAX, and the thousands separator as&nbsp;<wbr>&quot;_&quot;. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_parse_uint() <br/>
 Returns: Parsed number, or zero on error <br/>
 Type: unsigned int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start parsing at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Base (2-36) and flags, starting with USTR_FLAG_PARSE_NUM_ <br/>
 Type <code>[3]</code>: unsigned int </p>
<p> <br/>
 Parameter <code>[4]</code>: Return length of parsed number <br/>
 Type <code>[4]</code>: size_t * </p>
<p> <br/>
 Parameter <code>[5]</code>: Return error code, starting with USTR_TYPE_PARSE_NUM_ERR_ <br/>
 Type <code>[5]</code>: unsigned int * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_parse_ulongx()&nbsp;<wbr>with the minimum and maximum values taken as 0 and UINT_MAX, and the thousands separator as&nbsp;<wbr>&quot;_&quot;. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_parse_int() <br/>
 Returns: Parsed number, or zero on error <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start parsing at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Base (2-36) and flags, starting with USTR_FLAG_PARSE_NUM_ <br/>
 Type <code>[3]</code>: unsigned int </p>
<p> <br/>
 Parameter <code>[4]</code>: Return length of parsed number <br/>
 Type <code>[4]</code>: size_t * </p>
<p> <br/>
 Parameter <code>[5]</code>: Return error code, starting with USTR_TYPE_PARSE_NUM_ERR_ <br/>
 Type <code>[5]</code>: unsigned int * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_parse_ulongx()&nbsp;<wbr>with the minimum and maximum values taken as -INT_MIN and INT_MAX, and the thousands separator as&nbsp;<wbr>&quot;_&quot;. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_parse_ushort() <br/>
 Returns: Parsed number, or zero on error <br/>
 Type: unsigned short </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start parsing at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Base (2-36) and flags, starting with USTR_FLAG_PARSE_NUM_ <br/>
 Type <code>[3]</code>: unsigned int </p>
<p> <br/>
 Parameter <code>[4]</code>: Return length of parsed number <br/>
 Type <code>[4]</code>: size_t * </p>
<p> <br/>
 Parameter <code>[5]</code>: Return error code, starting with USTR_TYPE_PARSE_NUM_ERR_ <br/>
 Type <code>[5]</code>: unsigned int * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_parse_ulongx()&nbsp;<wbr>with the minimum and maximum values taken as 0 and USHRT_MAX, and the thousands separator as&nbsp;<wbr>&quot;_&quot;. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_parse_short() <br/>
 Returns: Parsed number, or zero on error <br/>
 Type: short </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start parsing at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Base (2-36) and flags, starting with USTR_FLAG_PARSE_NUM_ <br/>
 Type <code>[3]</code>: unsigned int </p>
<p> <br/>
 Parameter <code>[4]</code>: Return length of parsed number <br/>
 Type <code>[4]</code>: size_t * </p>
<p> <br/>
 Parameter <code>[5]</code>: Return error code, starting with USTR_TYPE_PARSE_NUM_ERR_ <br/>
 Type <code>[5]</code>: unsigned int * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like ustr_parse_ulongx()&nbsp;<wbr>with the minimum and maximum values taken as -SHRT_MIN and SHRT_MAX, and the thousands separator as&nbsp;<wbr>&quot;_&quot;. </p>
<h2>Misc shortcut helper functions for Ustrs</h2>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_ensure_owner() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function makes sure that the Ustr string is owned when it returns&nbsp;<wbr>(Ie. ustr_owner()&nbsp;<wbr>returns USTR_TRUE), or it fails to allocate. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_wstr() <br/>
 Returns: Writable pointer to the start of data in the Ustr, or NULL <br/>
 Type: char * </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling ustr_sc_ensure_owner(), to make sure the Ustr string is writable, and if that succeeds it returns ustr_wstr(). On failure it returns NULL. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_export_subustr() <br/>
 Returns: A pointer to newly allocated block of memory <br/>
 Type: char * </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Position in the Ustr <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 Parameter <code>[3]</code>: Length to export from the Ustr <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: Allocation function (like malloc) <br/>
 Type <code>[4]</code>: void *(*)(size_t) </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function allocates a block of memory of size Length&nbsp;<wbr>(Parameter[3])&nbsp;<wbr>+&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>using the provided allocation function&nbsp;<wbr>(Parameter[4])&nbsp;<wbr>and copies the data starting from Position&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>within the ustr. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_export() <br/>
 Returns: A pointer to newly allocated block of memory <br/>
 Type: char * </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Allocation function (like malloc) <br/>
 Type <code>[2]</code>: void *(*)(size_t) </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling ustr_sc_export_subustr()&nbsp;<wbr>with a position of 1 and a length of ustr_len(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustrp_sc_export_subustrp() <br/>
 Returns: A pointer to newly allocated block of memory <br/>
 Type: char * </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a Ustr pool object <br/>
 Type <code>[1]</code>: struct Ustr_pool * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[3]</code>: Position in the Ustr <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 Parameter <code>[4]</code>: Length to export from the Ustr <br/>
 Type <code>[4]</code>: size_t </p>
<p> <br/>
 Parameter <code>[5]</code>: Allocation function (like malloc), or NULL <br/>
 Type <code>[5]</code>: void *(*)(size_t) </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function allocates a block of memory of size Length&nbsp;<wbr>(Parameter[4])&nbsp;<wbr>+&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>using either the provided allocation function&nbsp;<wbr>(Parameter[5]), or from the pool object if the allocation function is NUL, and copies the data starting from Position&nbsp;<wbr>(Parameter[3])&nbsp;<wbr>within the ustr. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustrp_sc_export() <br/>
 Returns: A pointer to newly allocated block of memory <br/>
 Type: char * </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a Ustr pool object <br/>
 Type <code>[1]</code>: struct Ustr_pool * </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[3]</code>: Allocation function (like malloc) <br/>
 Type <code>[3]</code>: void *(*)(size_t) </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works like calling ustrp_sc_export_subustrp()&nbsp;<wbr>with a position of 1 and a length of ustrp_len(). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_reverse() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function reverses all the bytes in the Ustr string, so the last one becomes the first and the second to last becomes the second etc. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_tolower() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function changes any ASCII upper case bytes into ASCII lower case bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_toupper() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function changes any ASCII lower case bytes into ASCII upper case bytes. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_ltrim_chrs() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Array of bytes, containing trimming data <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of byte data <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function deletes the bytes at the begining of the Ustr&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>that are in the span&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>of the specificed length&nbsp;<wbr>(parameter[2]). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_ltrim() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string, containing trimming bytes <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_sc_ltrim_chrs()&nbsp;<wbr>and passed ustr_cstr()&nbsp;<wbr>and ustr_len()&nbsp;<wbr>values of the Ustr string&nbsp;<wbr>(Parameter[2]). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_ltrim_cstr() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant C-style string, containing trimming bytes <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_sc_ltrim_chrs()&nbsp;<wbr>and passed strlen()&nbsp;<wbr>as the length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_rtrim_chrs() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Array of bytes, containing trimming data <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of byte data <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function deletes the bytes at the end of the Ustr&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>that are in the span&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>of the specificed length&nbsp;<wbr>(parameter[2]). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_rtrim() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string, containing trimming bytes <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_sc_rtrim_chrs()&nbsp;<wbr>and passed ustr_cstr()&nbsp;<wbr>and ustr_len()&nbsp;<wbr>values of the Ustr string&nbsp;<wbr>(Parameter[2]). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_rtrim_cstr() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant C-style string, containing trimming bytes <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_sc_rtrim_chrs()&nbsp;<wbr>and passed strlen()&nbsp;<wbr>as the length. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_trim_chrs() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Array of bytes, containing trimming data <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 Parameter <code>[3]</code>: Length of byte data <br/>
 Type <code>[3]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function deletes the bytes at the begining or end of the Ustr&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>that are in the span&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>of the specificed length&nbsp;<wbr>(parameter[2]). </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>Calling this function is much more efficient than calling ustr_sc_rtrim_chrs()&nbsp;<wbr>and then ustr_sc_ltrim_chrs(), as both ends are trimmed in a single pass. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_trim() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant Ustr string, containing trimming bytes <br/>
 Type <code>[2]</code>: const struct Ustr * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_sc_trim_chrs()&nbsp;<wbr>and passed ustr_cstr()&nbsp;<wbr>and ustr_len()&nbsp;<wbr>values of the Ustr string&nbsp;<wbr>(Parameter[2]). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_sc_trim_cstr() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: A pointer to a constant C-style string, containing trimming bytes <br/>
 Type <code>[2]</code>: const char * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function works as if you had called ustr_sc_trim_chrs()&nbsp;<wbr>and passed strlen()&nbsp;<wbr>as the length. </p>
<h2>Adding binary data to a Ustr</h2>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_add_b_uint16() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Binary value to add to the Ustr <br/>
 Type <code>[2]</code>: uint_least16_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function adds a binary representation of a value&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>to the Ustr&nbsp;<wbr>(Parameter[1]). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_add_b_uint32() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Binary value to add to the Ustr <br/>
 Type <code>[2]</code>: uint_least32_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function adds a binary representation of a value&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>to the Ustr&nbsp;<wbr>(Parameter[1]). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_add_b_uint64() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Binary value to add to the Ustr <br/>
 Type <code>[2]</code>: uint_least64_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function adds a binary representation of a value&nbsp;<wbr>(Parameter[2])&nbsp;<wbr>to the Ustr&nbsp;<wbr>(Parameter[1]). </p>
<h2>Parsing binary data from a Ustr</h2>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_parse_b_uint16() <br/>
 Returns: uint_least16_t <br/>
 Type: uint_least16_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start parsing at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function parses a binary representation from a Ustr&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>&nbsp;<wbr>starting at the offset&nbsp;<wbr>(Parameter[2]). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_parse_b_uint32() <br/>
 Returns: uint_least32_t <br/>
 Type: uint_least32_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start parsing at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function parses a binary representation from a Ustr&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>&nbsp;<wbr>starting at the offset&nbsp;<wbr>(Parameter[2]). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_parse_b_uint64() <br/>
 Returns: uint_least64_t <br/>
 Type: uint_least64_t </p>
<p> <br/>
 Parameter <code>[1]</code>: A pointer to a constant Ustr string <br/>
 Type <code>[1]</code>: const struct Ustr * </p>
<p> <br/>
 Parameter <code>[2]</code>: Offset within string to start parsing at <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function parses a binary representation from a Ustr&nbsp;<wbr>(Parameter[1])&nbsp;<wbr>&nbsp;<wbr>starting at the offset&nbsp;<wbr>(Parameter[2]). </p>
<h2>Misc. functions</h2>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_realloc() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a pointer to a Ustr string <br/>
 Type <code>[1]</code>: struct Ustr ** </p>
<p> <br/>
 Parameter <code>[2]</code>: Size of allocation <br/>
 Type <code>[2]</code>: size_t </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function is re-sizes the Ustr to the specified size&nbsp;<wbr>(Parameter[2]). <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This is mostly used to shrink a sized Ustr that is now significantly smaller than it once was. Although this function can also grow a Ustr. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>To have a size that isn&#8217;t implied from the length the Ustr must store a size value as well as a length&nbsp;<wbr>(ustr_sized()&nbsp;<wbr>must return USTR_TRUE). </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_cntl_opt() <br/>
 Returns: Success or failure <br/>
 Type: int </p>
<p> <br/>
 Parameter <code>[1]</code>: Optional value starting with USTR_CNTL_OPT_ <br/>
 Type <code>[1]</code>: int </p>
<p> <br/>
 Parameter <code>[2]</code>: Arugments to option <br/>
 Type <code>[2]</code>: ... </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This function views and/or changes global Ustr options, like whether ustr&#8217;s have an implicit or explicit size&nbsp;<wbr>(USTR_CNTL_OPT_GET_HAS_SIZE). </p>
<h2>Simple Ustr pool API</h2>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_pool_ll_make() <br/>
 Returns: Pointer to a Ustr pool object <br/>
 Type: struct Ustr_pool * </p>
<p> <br/>
 Parameter <code>[1]</code>: Nothing <br/>
 Type <code>[1]</code>: void </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This allocates a new pool using the&nbsp;<wbr>&quot;linked list&quot;&nbsp;<wbr>strategy, each allocation in the pool is added to a linked list ... and any allocations not freed directly are freed by the pool when it is cleared or freed. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_pool_make_subpool() <br/>
 Returns: Pointer to a Ustr pool object <br/>
 Type: struct Ustr_pool * </p>
<p> <br/>
 Parameter <code>[1]</code>: struct Ustr_pool * <br/>
 Type <code>[1]</code>: struct Ustr_pool * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This allocates a new pool as a child of the passed in pool&nbsp;<wbr>(Parameter[1]), The pool can be freed and cleared independantly of the parent pool however free and clear operations on the parent pool are automatically applied to all child pools. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_pool_free() <br/>
 Returns: Nothing <br/>
 Type: void </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a Ustr pool object <br/>
 Type <code>[1]</code>: struct Ustr_pool * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This deallocates a pool, and all sub-pools. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This also operates on all sub-pools. </p>
<p> <br/>
 <br/>
 <code>Function: </code> ustr_pool_clear() <br/>
 Returns: Nothing <br/>
 Type: void </p>
<p> <br/>
 Parameter <code>[1]</code>: Pointer to a Ustr pool object <br/>
 Type <code>[1]</code>: struct Ustr_pool * </p>
<p> <br/>
 <code>Explanation:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This allows all the data in the pool to be reused, it may also free some/all of the data in the pool, from the pool API. </p>
<p> <code>Note:</code> </p>
<p> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>This also operates on all sub-pools.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ustr_const/">ustr_const</a></code>(3) </p>
