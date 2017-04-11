{
    'includes': {
      '../../../../../config.gypi',
    },
    'targets': [
      {
        'target_name': 'brcmjpeg_static',
        'type': 'static_library',
        'dependencies': [
          '<(DEPTH)/userland/interface/vcos/pthreads/vcos_pthreads.gyp:vcos_pthreads_static',
          '<(DEPTH)/userland/interface/mmal/core/mmal_core.gyp:mmal_core_static',
          '<(DEPTH)/userland/interface/mmal/util/mmal_util.gyp:mmal_util_static',
          '<(DEPTH)/userland/interface/mmal/vc/mmal_vc.gyp:mmal_vc_client_static',
          #'xyzzy',
          #'../bar/bar.gyp:bar',
        ],
        #'defines': [
        #  'DEFINE_FOO',
        #  'DEFINE_A_VALUE=value',
        #],
        'include_dirs': [
          '../..',
          '<(DEPTH)/userland/host_applications/linux/libs/sm',
        ],
        'sources': [
          'brcmjpeg.c',
        ],
      },
    ],
}
