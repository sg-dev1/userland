{
    'includes': {
      '../../../../../config.gypi',
    },
    'targets': [
      {
        'target_name': 'vcsm_static',
        'type': 'static_library',
        'dependencies': [
          '<(DEPTH)/userland/interface/vcos/pthreads/vcos_pthreads.gyp:vcos_pthreads_static',
          #'xyzzy',
          #'../bar/bar.gyp:bar',
        ],
        #'defines': [
        #  'DEFINE_FOO',
        #  'DEFINE_A_VALUE=value',
        #],
        'include_dirs': [
          '<(DEPTH)/userland',
          '<(DEPTH)/userland/interface/vcos/pthreads',
          #'<(DEPTH)/userland/interface/vcos/generic',
          #'<(DEPTH)/userland/interface/vcos/glibc',
          '<(DEPTH)/userland/host_applications/linux/kernel_headers',

        ],
        'sources': [
          'user-vcsm.c',
        ],
      },
    ],
}
