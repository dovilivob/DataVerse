import processing.video.*;

Movie m;
PrintWriter output;
int pixelSize = 2, catchSec = 260;
IntList colors;
StringList Frames;
int rate = 5;

void writeFile() {
  output = createWriter("Arrays.txt");
  for (int i=0; i<Frames.size(); i++) {
    output.print(Frames.get(i).toString());
  }
  output.close();
  exit();
}

void setup() {
  frameRate(rate);
  noCursor();
  colorMode(HSB);
  size(192, 108);
  Frames = new StringList();
  smooth();
  m = new Movie(this, "movie.mp4");
  m.play();
  m.volume(0);
}

void movieEvent(Movie m) {
  m.read();
}

void draw() {
  image(m, 0, 0, width, height);
  filter(GRAY);
  noStroke();
  colors = new IntList();
  for (int x = 0; x < getpixelPos(0); x++) {
    for (int y = 0; y < getpixelPos(1); y++) {
      colors.append(get(x * pixelSize, y * pixelSize) / - 1000000);
      fill(get(x * pixelSize, y * pixelSize));
      rect(x * pixelSize, y * pixelSize, pixelSize, pixelSize);
    }
  }
  Frames.append(colors.toString());
  if (frameCount > frameRate * catchSec && frameCount < frameRate * (catchSec + 1)) {
    writeFile();
  }
}


int getpixelPos(int xy) {
  if (xy == 0) {
    return width / pixelSize;
  } else {
    return height / pixelSize;
  }
}
