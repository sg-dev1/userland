{
    'includes': {
      '../../../../config.gypi',
    },
    'targets': [
      {
        'target_name': 'mmal_omx_static',
        'type': 'static_library',
        'dependencies': [
          '<(DEPTH)/userland/interface/vcos/pthreads/vcos_pthreads.gyp:vcos_pthreads_static',
          '<(DEPTH)/userland/interface/mmal/core/mmal_core.gyp:mmal_core_static',
          '<(DEPTH)/userland/interface/mmal/util/mmal_util.gyp:mmal_util_static',
          'mmal_omxutil'
        ],
        #'defines': [
        #  'DEFINE_FOO',
        #  'DEFINE_A_VALUE=value',
        #],
        'include_dirs': [
          '..',
        ],
        'sources': [
          'mmalomx_core.c',
          'mmalomx_logging.c',
          'mmalomx_commands.c',
          'mmalomx_buffer.c',
          'mmalomx_marks.c',
          'mmalomx_roles.c',
          'mmalomx_parameters.c',
          'mmalomx_registry.c',
        ],
      },
      {
        'target_name': 'mmal_omxutil',
        'type': 'static_library',
        'include_dirs': [
          '..',
        ],
        'sources': [
          'mmalomx_util_params.c',
          'mmalomx_util_params_audio.c',
          'mmalomx_util_params_video.c',
          'mmalomx_util_params_camera.c',
          'mmalomx_util_params_misc.c',
        ],
      },
    ],
}
