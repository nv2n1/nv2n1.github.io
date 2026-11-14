---
title: "sc_ipv2(3)"
name: "sc_ipv2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_ipv2/"
---

sc::IPV2 -

<h2>Synopsis</h2>



<h3>Public Types</h3>

<pre><code>enum Status { OK = 0,
              KeyNotFound = 1,
              OutOfBounds = 2,
              Malloc = 3,
              NotAnArray = 4,
              NotAScalar = 5,
              Type = 6,
              HasNoValue = 7,
              ValNotExpd = 8 }

enum { KEYWORD_LENGTH = 256 }

Public Member Functions void
read(std::istream &amp;, std::ostream &amp;, const char *filename = 0)

    void append_from_input(const char *, std::ostream &amp;)

        void done()

            const char *error_message(IPV2::Status)

                void error(const char *)

                    void warn(const char *)

                        void cwk_root()

                            void cwk_clear()

                                void cwk_add(const char *)

                                    void cwk_push()

                                        void cwk_pop()

                                            IPV2::Status boolean(const char *, int *, int, ...)

                                                IPV2::Status boolean_v(const char *, int *, int, int *)

                                                    int exist(const char *, int, ...)

                                                        int exist_v(const char *, int, int *)

                                                            IPV2::Status data(const char *, const char *, void *, int, ...)

                                                                IPV2::Status data_v(const char *, const char *, void *, int, int *)

                                                                    IPV2::Status classname(const char *, const char **, int, ...)

                                                                        IPV2::Status classname_v(const char *, const char **, int, int *)

                                                                            IPV2::Status truekeyword(const char *, const char **, int, ...)

                                                                                IPV2::Status truekeyword_v(const char *, const char **, int, int *)

                                                                                    IPV2::Status string(const char *, char **, int, ...)

                                                                                        IPV2::Status string_v(const char *, char **, int, int *)

                                                                                            IPV2::Status value(const char *, const char **, int, ...)

                                                                                                IPV2::Status value_v(const char *, const char **, int, int *)

                                                                                                    IPV2::Status construct_key_v(const char *, char *, int, int *)

                                                                                                        IPV2::Status count(const char *, int *, int, ...)

                                                                                                            IPV2::Status count_v(const char *, int *, int, int *)

                                                                                                                void print_keyword(std::ostream &amp;f = ExEnv::out0(), ip_keyword_tree_t *k = 0)

                                                                                                                    void print_tree(std::ostream &amp;f = ExEnv::out0(), ip_keyword_tree_t *k = 0)

                                                                                                                        void print_unseen(std::ostream &amp;f = ExEnv::out0(), ip_keyword_tree_t *k = 0)

                                                                                                                            int have_unseen(ip_keyword_tree_t *k = 0)

                                                                                                                                Static Public Member Functions
    static int have_global()

        static void set_global(IPV2 *)

            static IPV2 *global()
</code></pre>

<h2>Author</h2>

Generated automatically by Doxygen for MPQC from the source code.
