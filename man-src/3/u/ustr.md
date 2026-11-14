---
title: "ustr(3)"
name: "ustr"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustr/"
description: "ustr – ustr string library functions"
---

<p>ustr &#8211; ustr string library functions</p>
<h2>Synopsis</h2>
<pre><code>#include &quot;ustr.h&quot;

struct Ustr *USTR(void *);

struct Ustrp *USTRP(void *);

struct Ustr *USTR1(symbol, const char[]);

struct Ustr *USTR2(symbol, symbol, const char[]);

struct Ustr *USTR4(symbol, symbol, symbol, symbol, const char[]);

struct Ustr *USTR1_CHK(symbol, const char[]);

struct Ustr *USTR2_CHK(symbol, symbol, const char[]);

struct Ustr *USTR4_CHK(symbol, symbol, symbol, symbol, const char[]);

struct Ustr *USTRP1(symbol, const char[]);

struct Ustr *USTRP2(symbol, symbol, const char[]);

struct Ustrp *USTRP4(symbol, symbol, symbol, symbol, const char[]);

struct Ustr *USTRP1_CHK(symbol, const char[]);

struct Ustr *USTRP2_CHK(symbol, symbol, const char[]);

struct Ustrp *USTRP4_CHK(symbol, symbol, symbol, symbol, const char[]);
size_t USTR_SIZE_FIXED(size_t);

struct Ustr *ustr_init_fixed(void *, size_t, int, size_t);

struct Ustr *USTR_SC_INIT_AUTO(char[], int, size_t);

struct Ustr *USTR_SC_INIT_AUTO_OSTR(char[], int, size_t);
int ustr_assert_valid(Ustr *);

int ustr_assert_valid_subustr(Ustr *, size_t, size_t);

int USTR_CNTL_MALLOC_CHECK_BEG(int);

int USTR_CNTL_MALLOC_CHECK_LVL(void);

int USTR_CNTL_MALLOC_CHECK_MEM(void *);

int USTR_CNTL_MALLOC_CHECK_MEM_SZ(void *, size_t);

int USTR_CNTL_MALLOC_CHECK_MEM_MINSZ(void *, size_t);

int USTR_CNTL_MALLOC_CHECK_MEM_USTR(Ustr *);

int USTR_CNTL_MALLOC_CHECK_MEM_USTRP(Ustrp *);

int USTR_CNTL_MALLOC_CHECK_END(void);

int USTR_CNTL_MALLOC_CHECK_ADD(int);

int USTR_CNTL_MALLOC_CHECK_DEL(int);
size_t ustr_init_size(size_t, size_t, int, size_t);

struct Ustr *ustr_init_alloc(void *, size_t, size_t, size_t, int, int, size_t);

struct Ustr *ustr_dupx_empty(size_t, size_t, int, int);

struct Ustr *ustr_dup_empty(void);

struct Ustr *ustr_dupx_undef(size_t, size_t, int, int, size_t);

struct Ustr *ustr_dup_undef(size_t);

struct Ustr *ustr_dup(const struct Ustr *);

struct Ustr *ustr_dupx(size_t, size_t, int, int, const struct Ustr *);

struct Ustr *ustr_sc_dup(struct Ustr **);

struct Ustr *ustr_sc_dupx(size_t, size_t, int, int, struct Ustr **);

struct Ustr *ustr_dup_buf(const void *, size_t);

struct Ustr *ustr_dupx_buf(size_t, size_t, int, int, const void *, size_t);

struct Ustr *ustr_dup_cstr(const char *);

struct Ustr *ustr_dupx_cstr(size_t, size_t, int, int, const char *);

struct Ustr *USTR_DUP_OSTR(const char[]);

struct Ustr *USTR_DUP_OBJ(...);

struct Ustr *ustr_dup_subustr(const struct Ustr *, size_t, size_t);

struct Ustr *ustr_dupx_subustr(size_t, size_t, int, int, const struct Ustr *, size_t, size_t);

struct Ustr *ustr_dup_rep_chr(char, size_t);

struct Ustr *ustr_dupx_rep_chr(size_t, size_t, int, int, char, size_t);

struct Ustr *ustr_sc_vjoin(const struct Ustr *, const struct Ustr *, const struct Ustr *, va_list);

struct Ustr *ustr_sc_join(const struct Ustr *, const struct Ustr *, const struct Ustr *, ...);

struct Ustr *ustr_sc_vjoinx(size_t, size_t, int, int, const struct Ustr *, const struct Ustr *, const struct Ustr *, va_list);

struct Ustr *ustr_sc_joinx(size_t, size_t, int, int, const struct Ustr *, const struct Ustr *, const struct Ustr *, ...);

struct Ustr *ustr_sc_vconcat(const struct Ustr *, va_list);

struct Ustr *ustr_sc_concat(const struct Ustr *, ...);

struct Ustr *ustr_sc_vconcatx(size_t, size_t, int, int, const struct Ustr *, va_list);

struct Ustr *ustr_sc_concatx(size_t, size_t, int, int, const struct Ustr *, ...);
void ustr_free(struct Ustr *);

void ustrp_free(struct Ustr_pool *, struct Ustrp *);

void ustr_sc_free(struct Ustr **);

void ustr_sc_free2(struct Ustr **, struct Ustr *);

void ustr_sc_free_shared(struct Ustr **);

int ustr_del(struct Ustr **, size_t);

int ustr_del_subustr(struct Ustr **, size_t, size_t);

void ustr_sc_del(struct Ustr **);
int ustr_add_undef(struct Ustr **, size_t);

int ustr_add_buf(struct Ustr **, const void *, size_t);

int ustr_add_cstr(struct Ustr **, const char *);

int USTR_ADD_OSTR(struct Ustr **, const char[]);

int USTR_ADD_OBJ(struct Ustr **, ...);

int ustr_add(struct Ustr **, const struct Ustr *);

int ustr_add_subustr(struct Ustr **, const struct Ustr *, size_t, size_t);

int ustr_add_rep_chr(struct Ustr **, char, size_t);
int ustr_set_undef(struct Ustr **, size_t);

int ustr_set_empty(struct Ustr **);

int ustr_set_buf(struct Ustr **, const void *, size_t);

int ustr_set_cstr(struct Ustr **, const char *);

int USTR_SET_OSTR(struct Ustr **, const char[]);

int USTR_SET_OBJ(struct Ustr **, ...);

int ustr_set(struct Ustr **, const struct Ustr *);

int ustr_set_subustr(struct Ustr **, const struct Ustr *, size_t, size_t);

int ustr_set_rep_chr(struct Ustr **, char, size_t);
int ustr_ins_undef(struct Ustr **, size_t, size_t);

int ustr_ins_buf(struct Ustr **, size_t, const void *, size_t);

int ustr_ins_cstr(struct Ustr **, size_t, const char *);

int USTR_INS_OSTR(struct Ustr **, size_t, const char[]);

int USTR_INS_OBJ(struct Ustr **, size_t, ...);

int ustr_ins(struct Ustr **, size_t, const struct Ustr *);

int ustr_ins_subustr(struct Ustr **, size_t, const struct Ustr *, size_t, size_t);

int ustr_ins_rep_chr(struct Ustr **, size_t, char, size_t);
int ustr_add_vfmt_lim(struct Ustr **, size_t, const char *, va_list);

int ustr_add_vfmt(struct Ustr **, const char *, va_list);

int ustr_add_fmt_lim(struct Ustr **, size_t, const char *, ...);

int ustr_add_fmt(struct Ustr **, const char *, ...);

struct Ustr *ustr_dup_vfmt_lim(size_t, const char *, va_list);

struct Ustr *ustr_dup_vfmt(size_t, const char *, va_list);

struct Ustr *ustr_dup_fmt_lim(size_t, const char *, ...);

struct Ustr *ustr_dup_fmt(const char *, ...);

struct Ustr *ustr_dupx_fmt_lim(size_t, size_t, int, int, size_t, const char *, ...);

struct Ustr *ustr_dupx_fmt(size_t, size_t, int, int, const char *, ...);

int ustr_set_vfmt_lim(struct Ustr **, size_t, const char *, va_list);

int ustr_set_vfmt(struct Ustr **, const char *, va_list);

int ustr_set_fmt_lim(struct Ustr **, size_t, const char *, ...);

int ustr_set_fmt(struct Ustr **, const char *, ...);

int ustr_ins_vfmt_lim(struct Ustr **, size_t, size_t, const char *, va_list);

int ustr_ins_vfmt(struct Ustr **, size_t, const char *, va_list);

int ustr_ins_fmt_lim(struct Ustr **, size_t, size_t, const char *, ...);

int ustr_ins_fmt(struct Ustr **, size_t, const char *, ...);

int ustr_sub_vfmt_lim(struct Ustr **, size_t, size_t, const char *, va_list);

int ustr_sub_vfmt(struct Ustr **, size_t, const char *, va_list);

int ustr_sub_fmt_lim(struct Ustr **, size_t, size_t, const char *, ...);

int ustr_sub_fmt(struct Ustr **, size_t, const char *, ...);

int ustr_sc_sub_vfmt_lim(struct Ustr **, size_t, size_t, size_t, const char *, va_list);

int ustr_sc_sub_vfmt(struct Ustr **, size_t, size_t, const char *, va_list);

int ustr_sc_sub_fmt_lim(struct Ustr **, size_t, size_t, size_t, const char *, ...);

int ustr_sc_sub_fmt(struct Ustr **, size_t, size_t, const char *, ...);
size_t ustr_len(const struct Ustr *);

const char *ustr_cstr(const struct Ustr *);

char *ustr_wstr(struct Ustr *);

int ustr_alloc(const struct Ustr *);

int ustr_exact(const struct Ustr *);

int ustr_sized(const struct Ustr *);

int ustr_ro(const struct Ustr *);

int ustr_fixed(const struct Ustr *);

int ustr_enomem(const struct Ustr *);

int ustr_shared(const struct Ustr *);

int ustr_limited(const struct Ustr *);

int ustr_owner(const struct Ustr *);

size_t ustr_size(const struct Ustr *);

size_t ustr_size_alloc(const struct Ustr *);

size_t ustr_size_overhead(const struct Ustr *);

void ustr_conf(const struct Ustr *, size_t *, size_t *, int *, size_t *, size_t *);
int ustr_setf_enomem_err(struct Ustr *);

int ustr_setf_enomem_clr(struct Ustr *);

int ustr_setf_share(struct Ustr *);

int ustr_setf_owner(struct Ustr *);
int ustr_cmp_buf(const struct Ustr *, const void *, size_t);

int ustr_cmp(const struct Ustr *, const struct Ustr *);

int ustr_cmp_subustr(const struct Ustr *, const struct Ustr *, size_t, size_t);

int ustr_cmp_cstr(const struct Ustr *, const char *);

int ustr_cmp_fast_buf(const struct Ustr *, const void *, size_t);

int ustr_cmp_fast(const struct Ustr *, const struct Ustr *);

int ustr_cmp_fast_subustr(const struct Ustr *, const struct Ustr *, size_t, size_t);

int ustr_cmp_fast_cstr(const struct Ustr *, const char *);

int ustr_cmp_case_buf(const struct Ustr *, const void *, size_t);

int ustr_cmp_case(const struct Ustr *, const struct Ustr *);

int ustr_cmp_case_subustr(const struct Ustr *, const struct Ustr *, size_t, size_t);

int ustr_cmp_case_cstr(const struct Ustr *, const char *);

int ustr_cmp_eq(const struct Ustr *, const struct Ustr *);

int ustr_cmp_buf_eq(const struct Ustr *, const void *, size_t);

int ustr_cmp_subustr_eq(const struct Ustr *, const struct Ustr *, size_t, size_t);

int ustr_cmp_cstr_eq(const struct Ustr *, const char *);

int ustr_cmp_case_eq(const struct Ustr *, const struct Ustr *);

int ustr_cmp_case_buf_eq(const struct Ustr *, const void *, size_t);

int ustr_cmp_case_subustr_eq(const struct Ustr *, const struct Ustr *, size_t, size_t);

int ustr_cmp_case_cstr_eq(const struct Ustr *, const char *);

int ustr_cmp_prefix_eq(const struct Ustr *, const struct Ustr *);

int ustr_cmp_prefix_buf_eq(const struct Ustr *, const void *, size_t);

int ustr_cmp_prefix_cstr_eq(const struct Ustr *, const char *);

int ustr_cmp_prefix_subustr_eq(const struct Ustr *, const struct Ustr *, size_t, size_t);

int ustr_cmp_case_prefix_eq(const struct Ustr *, const struct Ustr *);

int ustr_cmp_case_prefix_buf_eq(const struct Ustr *, const void *, size_t);

int ustr_cmp_case_prefix_cstr_eq(const struct Ustr *, const char *);

int ustr_cmp_case_prefix_subustr_eq(const struct Ustr *, const struct Ustr *, size_t, size_t);

int ustr_cmp_suffix_eq(const struct Ustr *, const struct Ustr *);

int ustr_cmp_suffix_buf_eq(const struct Ustr *, const void *, size_t);

int ustr_cmp_suffix_cstr_eq(const struct Ustr *, const char *);

int ustr_cmp_suffix_subustr_eq(const struct Ustr *, const struct Ustr *, size_t, size_t);

int ustr_cmp_case_suffix_eq(const struct Ustr *, const struct Ustr *);

int ustr_cmp_case_suffix_buf_eq(const struct Ustr *, const void *, size_t);

int ustr_cmp_case_suffix_cstr_eq(const struct Ustr *, const char *);

int ustr_cmp_case_suffix_subustr_eq(const struct Ustr *, const struct Ustr *, size_t, size_t);
size_t ustr_srch_chr_fwd(const struct Ustr *, size_t, char);

size_t ustr_srch_chr_rev(const struct Ustr *, size_t, char);

size_t ustr_srch_buf_fwd(const struct Ustr *, size_t, const void *, size_t);

size_t ustr_srch_buf_rev(const struct Ustr *, size_t, const void *, size_t);

size_t ustr_srch_fwd(const struct Ustr *, size_t, const struct Ustr *);

size_t ustr_srch_rev(const struct Ustr *, size_t, const struct Ustr *);

size_t ustr_srch_cstr_fwd(const struct Ustr *, size_t, const char *);

size_t ustr_srch_cstr_rev(const struct Ustr *, size_t, const char *);

size_t ustr_srch_subustr_fwd(const struct Ustr *, size_t, const struct Ustr *, size_t, size_t);

size_t ustr_srch_subustr_rev(const struct Ustr *, size_t, const struct Ustr *, size_t, size_t);

size_t ustr_srch_case_chr_fwd(const struct Ustr *, size_t, char);

size_t ustr_srch_case_chr_rev(const struct Ustr *, size_t, char);

size_t ustr_srch_case_buf_fwd(const struct Ustr *, size_t, const void *, size_t);

size_t ustr_srch_case_buf_rev(const struct Ustr *, size_t, const void *, size_t);

size_t ustr_srch_case_fwd(const struct Ustr *, size_t, const struct Ustr *);

size_t ustr_srch_case_rev(const struct Ustr *, size_t, const struct Ustr *);

size_t ustr_srch_case_cstr_fwd(const struct Ustr *, size_t, const char *);

size_t ustr_srch_case_cstr_rev(const struct Ustr *, size_t, const char *);

size_t ustr_srch_case_subustr_fwd(const struct Ustr *, size_t, const struct Ustr *, size_t, size_t);

size_t ustr_srch_case_subustr_rev(const struct Ustr *, size_t, const struct Ustr *, size_t, size_t);
size_t ustr_spn_chr_fwd(const struct Ustr *, size_t, char);

size_t ustr_spn_chr_rev(const struct Ustr *, size_t, char);

size_t ustr_spn_chrs_fwd(const struct Ustr *, size_t, const char *, size_t);

size_t ustr_spn_chrs_rev(const struct Ustr *, size_t, const char *, size_t);

size_t ustr_spn_fwd(const struct Ustr *, size_t, const struct Ustr *);

size_t ustr_spn_rev(const struct Ustr *, size_t, const struct Ustr *);

size_t ustr_spn_cstr_fwd(const struct Ustr *, size_t, const char *);

size_t ustr_spn_cstr_rev(const struct Ustr *, size_t, const char *);

size_t ustr_cspn_chr_fwd(const struct Ustr *, size_t, char);

size_t ustr_cspn_chr_rev(const struct Ustr *, size_t, char);

size_t ustr_cspn_chrs_fwd(const struct Ustr *, size_t, const char *, size_t);

size_t ustr_cspn_chrs_rev(const struct Ustr *, size_t, const char *, size_t);

size_t ustr_cspn_fwd(const struct Ustr *, size_t, const struct Ustr *);

size_t ustr_cspn_rev(const struct Ustr *, size_t, const struct Ustr *);

size_t ustr_cspn_cstr_fwd(const struct Ustr *, size_t, const char *);

size_t ustr_cspn_cstr_rev(const struct Ustr *, size_t, const char *);

size_t ustr_utf8_spn_chrs_fwd(const struct Ustr *, size_t, const char *, size_t);

size_t ustr_utf8_spn_chrs_rev(const struct Ustr *, size_t, const char *, size_t);

size_t ustr_utf8_spn_fwd(const struct Ustr *, size_t, const struct Ustr *);

size_t ustr_utf8_spn_rev(const struct Ustr *, size_t, const struct Ustr *);

size_t ustr_utf8_spn_cstr_fwd(const struct Ustr *, size_t, const char *);

size_t ustr_utf8_spn_cstr_rev(const struct Ustr *, size_t, const char *);

size_t ustr_utf8_cspn_chrs_fwd(const struct Ustr *, size_t, const char *, size_t);

size_t ustr_utf8_cspn_chrs_rev(const struct Ustr *, size_t, const char *, size_t);

size_t ustr_utf8_cspn_fwd(const struct Ustr *, size_t, const struct Ustr *);

size_t ustr_utf8_cspn_rev(const struct Ustr *, size_t, const struct Ustr *);

size_t ustr_utf8_cspn_cstr_fwd(const struct Ustr *, size_t, const char *);

size_t ustr_utf8_cspn_cstr_rev(const struct Ustr *, size_t, const char *);
int ustr_io_get(struct Ustr **, FILE *, size_t, size_t *);

int ustr_io_getfile(struct Ustr **, FILE *);

int ustr_io_getfilename(struct Ustr **, const char *);

int ustr_io_getdelim(struct Ustr **, FILE *, char);

int ustr_io_getline(struct Ustr **, FILE *);

int ustr_io_put(struct Ustr **, FILE *, size_t);

int ustr_io_putline(struct Ustr **, FILE *, size_t);

int ustr_io_putfile(struct Ustr **, FILE *);

int ustr_io_putfileline(struct Ustr **, FILE *);

int ustr_io_putfilename(struct Ustr **, const char *, const char *);
int ustr_sub_undef(struct Ustr **, size_t, size_t);

int ustr_sub_buf(struct Ustr **, size_t, const void *, size_t);

int ustr_sub_cstr(struct Ustr **, size_t, const char *);

int USTR_SUB_OSTR(struct Ustr **, size_t, const char[]);

int USTR_SUB_OBJ(struct Ustr **, size_t, ...);

int ustr_sub(struct Ustr **, size_t, const struct Ustr *);

int ustr_sub_subustr(struct Ustr **, size_t, const struct Ustr *, size_t, size_t);

int ustr_sc_sub_undef(struct Ustr **, size_t, size_t, size_t);

int ustr_sc_sub_buf(struct Ustr **, size_t, size_t, const void *, size_t);

int ustr_sc_sub_cstr(struct Ustr **, size_t, size_t, const char *);

int ustr_sc_sub(struct Ustr **, size_t, size_t, const struct Ustr *);

int ustr_sc_sub_subustr(struct Ustr **, size_t, size_t, const struct Ustr *, size_t, size_t);

int USTR_SC_SUB_OSTR(struct Ustr **, size_t, size_t, const char[]);

int USTR_SC_SUB_OBJ(struct Ustr **, size_t, size_t, ...);

size_t ustr_replace_buf(struct Ustr **, const void *, size_t, const void *, size_t, size_t);

size_t ustr_replace_cstr(struct Ustr **, const char *, const char *, size_t);

int ustr_replace(struct Ustr **, const struct Ustr *, const struct Ustr *, size_t);

size_t ustr_replace_rep_chr(struct Ustr **ps1, char, size_t, char, size_t nlen, size_t lim);
struct Ustr *ustr_split_buf(const struct Ustr *, size_t *, const void *, size_t, struct Ustr *, unsigned int);

struct Ustr *ustr_split(const struct Ustr *, size_t *, const struct Ustr *, struct Ustr *, unsigned int);

struct Ustr *ustr_split_cstr(const struct Ustr *, size_t *, const char *, struct Ustr *, unsigned int);

struct Ustr *ustr_split_spn_chrs(const struct Ustr *, size_t *, const char *, size_t, struct Ustr *, unsigned int);

struct Ustr *ustr_split_spn_cstr(const struct Ustr *, size_t *, const char *, struct Ustr *, unsigned int);

struct Ustr *ustr_split_spn(const struct Ustr *, size_t *, const struct Ustr *, struct Ustr *, unsigned int);
int ustr_utf8_valid(const struct Ustr *);

size_t ustr_utf8_len(const struct Ustr *);

ssize_t ustr_utf8_width(const struct Ustr *);

size_t ustr_utf8_chars2bytes(const struct Ustr *, size_t, size_t, size_t *);

size_t ustr_utf8_bytes2chars(const struct Ustr *, size_t, size_t, size_t *);

int ustr_sc_utf8_reverse(struct Ustr **);
uintmax_t ustr_parse_uintmaxx(const struct Ustr *, size_t, unsigned int, uintmax_t, uintmax_t, const char *, size_t *, unsigned int *);

uintmax_t ustr_parse_uintmax(const struct Ustr *, size_t, unsigned int, size_t *, unsigned int *);

intmax_t ustr_parse_intmax(const struct Ustr *, size_t, unsigned int, size_t *, unsigned int *);

unsigned long ustr_parse_ulongx(const struct Ustr *, size_t, unsigned int, unsigned long, unsigned long, const char *, size_t *, unsigned int *);

unsigned long ustr_parse_ulong(const struct Ustr *, size_t, unsigned int, size_t *, unsigned int *);

long ustr_parse_long(const struct Ustr *, size_t, unsigned int, size_t *, unsigned int *);

unsigned int ustr_parse_uint(const struct Ustr *, size_t, unsigned int, size_t *, unsigned int *);

int ustr_parse_int(const struct Ustr *, size_t, unsigned int, size_t *, unsigned int *);

unsigned short ustr_parse_ushort(const struct Ustr *, size_t, unsigned int, size_t *, unsigned int *);

short ustr_parse_short(const struct Ustr *, size_t, unsigned int, size_t *, unsigned int *);
int ustr_sc_ensure_owner(struct Ustr **);

char *ustr_sc_wstr(struct Ustr **);

char *ustr_sc_export_subustr(const struct Ustr *, size_t, size_t, void *(*)(size_t));

char *ustr_sc_export(const struct Ustr *, void *(*)(size_t));

char *ustrp_sc_export_subustrp(struct Ustr_pool *, const struct Ustr *, size_t, size_t, void *(*)(size_t));

char *ustrp_sc_export(struct Ustr_pool *, const struct Ustr *, void *(*)(size_t));

int ustr_sc_reverse(struct Ustr **);

int ustr_sc_tolower(struct Ustr **);

int ustr_sc_toupper(struct Ustr **);

int ustr_sc_ltrim_chrs(struct Ustr **, const char *, size_t);

int ustr_sc_ltrim(struct Ustr **, const struct Ustr *);

int ustr_sc_ltrim_cstr(struct Ustr **, const char *);

int ustr_sc_rtrim_chrs(struct Ustr **, const char *, size_t);

int ustr_sc_rtrim(struct Ustr **, const struct Ustr *);

int ustr_sc_rtrim_cstr(struct Ustr **, const char *);

int ustr_sc_trim_chrs(struct Ustr **, const char *, size_t);

int ustr_sc_trim(struct Ustr **, const struct Ustr *);

int ustr_sc_trim_cstr(struct Ustr **, const char *);
int ustr_add_b_uint16(struct Ustr **, uint_least16_t);

int ustr_add_b_uint32(struct Ustr **, uint_least32_t);

int ustr_add_b_uint64(struct Ustr **, uint_least64_t);
uint_least16_t ustr_parse_b_uint16(const struct Ustr *, size_t);

uint_least32_t ustr_parse_b_uint32(const struct Ustr *, size_t);

uint_least64_t ustr_parse_b_uint64(const struct Ustr *, size_t);
int ustr_realloc(struct Ustr **, size_t);

int ustr_cntl_opt(int, ...);
struct Ustr_pool *ustr_pool_ll_make(void);

struct Ustr_pool *ustr_pool_make_subpool(struct Ustr_pool *);

void ustr_pool_free(struct Ustr_pool *);

void ustr_pool_clear(struct Ustr_pool *);</code></pre>
<p> create constant/read-only strings, and USTR_SC_INIT_AUTO() to create strings that use stack space upto a certain amount.<br />
&nbsp;<wbr>Use is somewhat unique in that, by default, it has an average overhead of only 55% overhead over strdup(), for strings in the range of 0 to 20 bytes. Or, to put it another way it only uses 8 bytes to store a 2 byte string where strdup() uses 3.</p>
<h2>Creating read-only Ustr functions</h2>
<p><code>Function: </code> USTR()<br />
 Returns: Ustr string<br />
 Type: struct Ustr * </p>
<p> Parameter<code>[1]</code>: Pointer to Ustr data<br />
 Type<code>[1]</code>: void * </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This macro function is normally used with the empty string&nbsp;<wbr>&quot;&quot;. </p>
<p> <code>Note:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>There is basically just a simple cast behind the macro. </p>
<p> <code>Function: </code> USTRP()<br />
 Returns: Ustrp string<br />
 Type: struct Ustrp * </p>
<p> Parameter<code>[1]</code>: Pointer to Ustrp data<br />
 Type<code>[1]</code>: void * </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This macro function is normally used with the empty string&nbsp;<wbr>&quot;&quot;. </p>
<p> <code>Note:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>There is basically just a simple cast behind the macro. </p>
<p> <code>Function: </code> USTR1()<br />
 Returns: Ustr string<br />
 Type: struct Ustr * </p>
<p> Parameter<code>[1]</code>: Encoded number of the length of Ustr string<br />
 Type<code>[1]</code>: symbol </p>
<p> Parameter<code>[2]</code>: Data for Ustr string<br />
 Type<code>[2]</code>: const char[] </p>
<p> <code>Explanation:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This macro function simplifies the creation of read-only Ustr string&#8217;s. And is normally used like&#8230; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>USTR1(,&nbsp;<wbr>&quot;abcd&quot;) </p>
<p>&nbsp;<wbr>&#8230;it is worth pointing out that running with debugging turned on<br />
&nbsp;<wbr>(USTR_CONF_USE_ASSERT)&nbsp;<wbr>will complain if the length isn&#8217;t encoded correctly, as in&#8230; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>USTR1(,&nbsp;<wbr>&quot;abcd&quot;) </p>
<p>&nbsp;<wbr>&#8230;here ustr_assert_valid()&nbsp;<wbr>will fail, which is called before most functions do<br />
&nbsp;<wbr>anything in debugging mode. Note also that extra debugging&nbsp;<wbr>(USTR_CONF_USE_EOS_MARK)&nbsp;<wbr>will still catch cases like&#8230; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>USTR1(,&nbsp;<wbr>&quot;abc
