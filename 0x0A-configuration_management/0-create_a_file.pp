#the code will create a file name inside tmp/Directory

file { '/tmp/school':
   content => 'I love puppet',
   mode    => '0744',
   Owner   => 'www-data',
   group   => 'www-data',
}
