{
    'includes': {
      '../../../../config.gypi',
    },
    'targets': [
      {
        'target_name': 'mmal_vc_client_static',
        'type': 'static_library',
        'dependencies': [
          '<(DEPTH)/userland/interface/vcos/pthreads/vcos_pthreads.gyp:vcos_pthreads_static',
          '<(DEPTH)/userland/interface/vchiq_arm/vchiq_arm.gyp:vchiq_arm_static',
          '<(DEPTH)/userland/host_applications/linux/libs/sm/vcsm.gyp:vcsm_static',
        ],
        'defines': [
          'ENABLE_MMAL_VCSM',
        ],
        'include_dirs': [
          '..',
          '<(DEPTH)/userland/interface/vchiq_arm',
          '<(DEPTH)/userland/host_applications/linux/libs/sm',
        ],
        'sources': [
          'mmal_vc_client.c',
          'mmal_vc_shm.c',
          'mmal_vc_api.c',
          'mmal_vc_opaque_alloc.c',
          'mmal_vc_msgnames.c',
          'mmal_vc_api_drm.c',
        ],
      },
    ],
}
