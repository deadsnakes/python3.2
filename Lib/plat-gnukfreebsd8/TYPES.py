# Generated by h2py from /usr/include/sys/types.h
_SYS_TYPES_H = 1

# Included from features.h
_FEATURES_H = 1
__USE_ANSI = 1
__FAVOR_BSD = 1
_ISOC99_SOURCE = 1
_POSIX_SOURCE = 1
_POSIX_C_SOURCE = 200809
_XOPEN_SOURCE = 700
_XOPEN_SOURCE_EXTENDED = 1
_LARGEFILE64_SOURCE = 1
_BSD_SOURCE = 1
_SVID_SOURCE = 1
_ATFILE_SOURCE = 1
_BSD_SOURCE = 1
_SVID_SOURCE = 1
__USE_ISOC99 = 1
__USE_ISOC95 = 1
_POSIX_SOURCE = 1
_POSIX_C_SOURCE = 2
_POSIX_C_SOURCE = 199506
_POSIX_C_SOURCE = 200112
_POSIX_C_SOURCE = 200809
__USE_POSIX_IMPLICITLY = 1
__USE_POSIX = 1
__USE_POSIX2 = 1
__USE_POSIX199309 = 1
__USE_POSIX199506 = 1
__USE_XOPEN2K = 1
__USE_ISOC99 = 1
__USE_XOPEN2K8 = 1
_ATFILE_SOURCE = 1
__USE_XOPEN = 1
__USE_XOPEN_EXTENDED = 1
__USE_UNIX98 = 1
_LARGEFILE_SOURCE = 1
__USE_XOPEN2K8 = 1
__USE_XOPEN2K = 1
__USE_ISOC99 = 1
__USE_XOPEN_EXTENDED = 1
__USE_LARGEFILE = 1
__USE_LARGEFILE64 = 1
__USE_FILE_OFFSET64 = 1
__USE_MISC = 1
__USE_BSD = 1
__USE_SVID = 1
__USE_ATFILE = 1
__USE_GNU = 1
__USE_REENTRANT = 1
__USE_FORTIFY_LEVEL = 2
__USE_FORTIFY_LEVEL = 1
__USE_FORTIFY_LEVEL = 0

# Included from bits/predefs.h
__STDC_IEC_559__ = 1
__STDC_IEC_559_COMPLEX__ = 1
__STDC_ISO_10646__ = 200009
__GNU_LIBRARY__ = 6
__GLIBC__ = 2
__GLIBC_MINOR__ = 11
__GLIBC_HAVE_LONG_LONG = 1

# Included from sys/cdefs.h
_SYS_CDEFS_H = 1
def __NTH(fct): return fct

def __NTH(fct): return fct

def __P(args): return args

def __PMT(args): return args

def __STRING(x): return #x

def __bos(ptr): return __builtin_object_size (ptr, __USE_FORTIFY_LEVEL > 1)

def __bos0(ptr): return __builtin_object_size (ptr, 0)

def __warnattr(msg): return __attribute__((__warning__ (msg)))

__flexarr = []
__flexarr = [0]
__flexarr = []
__flexarr = [1]
def __ASMNAME(cname): return __ASMNAME2 (__USER_LABEL_PREFIX__, cname)

def __attribute__(xyz): return

def __attribute_format_arg__(x): return __attribute__ ((__format_arg__ (x)))

def __attribute_format_arg__(x): return


# Included from bits/wordsize.h
__WORDSIZE = 32
__LDBL_COMPAT = 1
def __LDBL_REDIR_DECL(name): return \

__USE_LARGEFILE = 1
__USE_LARGEFILE64 = 1
__USE_EXTERN_INLINES = 1
__USE_EXTERN_INLINES_IN_LIBC = 1

# Included from gnu/stubs.h

# Included from bits/types.h
_BITS_TYPES_H = 1
__S32_TYPE = int
__SWORD_TYPE = int
__SLONG32_TYPE = int

# Included from bits/typesizes.h
_BITS_TYPESIZES_H = 1
__PID_T_TYPE = __S32_TYPE
__CLOCK_T_TYPE = __S32_TYPE
__SWBLK_T_TYPE = __S32_TYPE
__CLOCKID_T_TYPE = __S32_TYPE
__TIMER_T_TYPE = __S32_TYPE
__SSIZE_T_TYPE = __SWORD_TYPE
__FD_SETSIZE = 1024

# Included from time.h
_TIME_H = 1

# Included from bits/time.h
_BITS_TIME_H = 1
CLOCKS_PER_SEC = 1000000
CLK_TCK = 128
CLOCK_REALTIME = 0
CLOCK_PROCESS_CPUTIME_ID = 2
CLOCK_THREAD_CPUTIME_ID = 3
CLOCK_MONOTONIC = 4
CLOCK_VIRTUAL = 1
CLOCK_PROF = 2
CLOCK_UPTIME = 5
CLOCK_UPTIME_PRECISE = 7
CLOCK_UPTIME_FAST = 8
CLOCK_REALTIME_PRECISE = 9
CLOCK_REALTIME_FAST = 10
CLOCK_MONOTONIC_PRECISE = 11
CLOCK_MONOTONIC_FAST = 12
CLOCK_SECOND = 13
TIMER_RELTIME = 0
TIMER_ABSTIME = 1
_STRUCT_TIMEVAL = 1
CLK_TCK = CLOCKS_PER_SEC
__clock_t_defined = 1
__time_t_defined = 1
__clockid_t_defined = 1
__timer_t_defined = 1
__timespec_defined = 1

# Included from xlocale.h
_XLOCALE_H = 1
def __isleap(year): return \

__BIT_TYPES_DEFINED__ = 1

# Included from endian.h
_ENDIAN_H = 1
__LITTLE_ENDIAN = 1234
__BIG_ENDIAN = 4321
__PDP_ENDIAN = 3412

# Included from bits/endian.h
__BYTE_ORDER = __LITTLE_ENDIAN
__FLOAT_WORD_ORDER = __BYTE_ORDER
LITTLE_ENDIAN = __LITTLE_ENDIAN
BIG_ENDIAN = __BIG_ENDIAN
PDP_ENDIAN = __PDP_ENDIAN
BYTE_ORDER = __BYTE_ORDER

# Included from bits/byteswap.h
_BITS_BYTESWAP_H = 1
def __bswap_constant_16(x): return \

def __bswap_16(x): return \

def __bswap_16(x): return \

def __bswap_constant_32(x): return \

def __bswap_32(x): return \

def __bswap_32(x): return \

def __bswap_32(x): return \

def __bswap_constant_64(x): return \

def __bswap_64(x): return \

def htobe16(x): return __bswap_16 (x)

def htole16(x): return (x)

def be16toh(x): return __bswap_16 (x)

def le16toh(x): return (x)

def htobe32(x): return __bswap_32 (x)

def htole32(x): return (x)

def be32toh(x): return __bswap_32 (x)

def le32toh(x): return (x)

def htobe64(x): return __bswap_64 (x)

def htole64(x): return (x)

def be64toh(x): return __bswap_64 (x)

def le64toh(x): return (x)

def htobe16(x): return (x)

def htole16(x): return __bswap_16 (x)

def be16toh(x): return (x)

def le16toh(x): return __bswap_16 (x)

def htobe32(x): return (x)

def htole32(x): return __bswap_32 (x)

def be32toh(x): return (x)

def le32toh(x): return __bswap_32 (x)

def htobe64(x): return (x)

def htole64(x): return __bswap_64 (x)

def be64toh(x): return (x)

def le64toh(x): return __bswap_64 (x)


# Included from sys/select.h
_SYS_SELECT_H = 1

# Included from bits/select.h
def __FD_ZERO(fdsp): return \

def __FD_ZERO(set): return \


# Included from bits/sigset.h
_SIGSET_H_types = 1
_SIGSET_H_fns = 1
def __sigword(sig): return (((sig) - 1) >> 5)

def __sigemptyset(set): return \

def __sigfillset(set): return \

def __sigisemptyset(set): return \

def __FDELT(d): return ((d) / __NFDBITS)

FD_SETSIZE = __FD_SETSIZE
def FD_ZERO(fdsetp): return __FD_ZERO (fdsetp)


# Included from sys/sysmacros.h
_SYS_SYSMACROS_H = 1
def minor(dev): return ((int)((dev) & (-65281)))

def gnu_dev_major(dev): return major (dev)

def gnu_dev_minor(dev): return minor (dev)


# Included from bits/pthreadtypes.h
_BITS_PTHREADTYPES_H = 1

# Included from bits/sched.h
SCHED_OTHER = 2
SCHED_FIFO = 1
SCHED_RR = 3
CSIGNAL = 0x000000ff
CLONE_VM = 0x00000100
CLONE_FS = 0x00000200
CLONE_FILES = 0x00000400
CLONE_SIGHAND = 0x00000800
CLONE_PTRACE = 0x00002000
CLONE_VFORK = 0x00004000
CLONE_SYSVSEM = 0x00040000
__defined_schedparam = 1
__CPU_SETSIZE = 128
def __CPUELT(cpu): return ((cpu) / __NCPUBITS)

def __CPU_ALLOC_SIZE(count): return \

def __CPU_ALLOC(count): return __sched_cpualloc (count)

def __CPU_FREE(cpuset): return __sched_cpufree (cpuset)

