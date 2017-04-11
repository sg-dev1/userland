{
    'includes': {
      '../../../../config.gypi',
    },
    'targets': [
      {
        'target_name': 'vcos_pthreads_static',
        'type': 'static_library',
        #'dependencies': [
        #  'xyzzy',
        #  '../bar/bar.gyp:bar',
        #],
        #'defines': [
        #  'DEFINE_FOO',
        #  'DEFINE_A_VALUE=value',
        #],
        'include_dirs': [
          '..',
        ],
        # dynamic link with pthread and rt  (for shared library also dl is needed)
        'direct_dependent_settings': {
          'linkflags': [
            'pthread',
            'rt',
          ],
        },
        'sources': [
          'vcos_pthreads.c',
          'vcos_dlfcn.c',
          '../glibc/vcos_backtrace.c',
          '../generic/vcos_generic_event_flags.c',
          '../generic/vcos_mem_from_malloc.c',
          '../generic/vcos_generic_named_sem.c',
          '../generic/vcos_generic_safe_string.c',
          '../generic/vcos_generic_reentrant_mtx.c',
          '../generic/vcos_abort.c',
          '../generic/vcos_cmd.c',
          '../generic/vcos_init.c',
          '../generic/vcos_msgqueue.c',
          '../generic/vcos_logcat.c',
          '../generic/vcos_generic_blockpool.c',
        ],
      },
    ],
}
