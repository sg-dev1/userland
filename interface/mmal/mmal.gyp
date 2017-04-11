{
    'includes': {
      '../../../config.gypi',
    },
    'targets': [
      {
        'target_name': 'mmal_static',
        'type': 'static_library',
        'dependencies': [
          '<(DEPTH)/userland/interface/mmal/core/mmal_core.gyp:mmal_core_static',
          '<(DEPTH)/userland/interface/mmal/util/mmal_util.gyp:mmal_util_static',
          '<(DEPTH)/userland/interface/mmal/vc/mmal_vc.gyp:mmal_vc_client_static',
          '<(DEPTH)/userland/interface/mmal/components/mmal_components.gyp:mmal_components_static',
          '<(DEPTH)/userland/interface/mmal/openmaxil/openmaxil.gyp:mmal_omx_static',
          '<(DEPTH)/userland/interface/mmal/client/brcmjpeg/brcmjpeg.gyp:brcmjpeg_static',
          '<(DEPTH)/userland/interface/vcos/pthreads/vcos_pthreads.gyp:vcos_pthreads_static',
        ],
        #'defines': [
        #  'DEFINE_FOO',
        #  'DEFINE_A_VALUE=value',
        #],
        'include_dirs': [
        ],
        #'sources': [
        #  'main.cpp',
        #  'mmal_component.cpp',
        #],
      },
    ],
}
