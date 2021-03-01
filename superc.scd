
x = File.open("~/Documents/dataanalys/np.txt".standardizePath, "r");
t = x.readAllString.split()


b = Array.fill(2000, { arg i; t[i].split($.).asInt });


~data1 = all {: x[0], x <- b };
~data2 = all {: x[1], x <- b };
~data3 = all {: x[2], x <- b };
~data4 = all {: x[3], x <- b };
~data1.normalize(0,12);
(
// send a synth def to server
SynthDef("bass", { arg out = 0,freq = 440, sawFreq = 220.0;
    Out.ar(out, SyncSaw.ar(freq, sawFreq, 0.1));
}).add;
)

y = Synth.new("bass");