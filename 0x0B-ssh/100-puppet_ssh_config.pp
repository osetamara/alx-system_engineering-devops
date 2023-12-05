#!/usr/bin/env bash
#using puppet to make changes to our configuration file


file { 'etc/ssh/ssh_config':
        ensure => present,
content =>"hello world
          #ssh client configuration
          host*
          IdentityFile ~/.ssh/school
          passwordAuthentication no
}
