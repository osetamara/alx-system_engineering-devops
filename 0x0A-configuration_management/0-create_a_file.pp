#the code will create a file name inside tmp/Directory
file { '/tmp/school':
   ensure  => 'file',
   content => 'I love puppet',
   mode    => '07744',
   Owner   => 'www-data',
   group   => 'www-data',
}
