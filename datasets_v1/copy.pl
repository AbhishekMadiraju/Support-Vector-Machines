open(IN,shift);
while(<IN>){
  chomp $_;
  $f=$_;
  system "mkdir $f";
  `cp ../$f/data $f/`;
  `cp ../$f/trueclass $f/`;
  `cp ../$f/random_class.0 $f/`;
  `cp ../$f/random_class.1 $f/`;
  `cp ../$f/random_class.2 $f/`;
  `cp ../$f/random_class.3 $f/`;
  `cp ../$f/random_class.4 $f/`;
  `cp ../$f/random_class.5 $f/`;
  `cp ../$f/random_class.6 $f/`;
  `cp ../$f/random_class.7 $f/`;
  `cp ../$f/random_class.8 $f/`;
  `cp ../$f/random_class.9 $f/`;
}
