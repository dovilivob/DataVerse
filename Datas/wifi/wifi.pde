import processing.video.*;

Movie m;
PrintWriter output;
String result = "";
int standardX = 50;
int rate = 10;
int catchSec = 240;

void writeFile() {
  output = createWriter("result.json");
  output.print("{\"rate\":"+str(rate)+",\"wifi-data\":["+result.substring(1)+"]}");
  output.close();
  exit();
}

void setup() {
  frameRate(rate);
  //noCursor();
  colorMode(HSB);
  size(192, 108);
  smooth();
  noStroke();
  m = new Movie(this, "movie.mp4");
  m.play();
  m.volume(0);
}

void movieEvent(Movie m) {
  m.read();
}
void draw() {
  background(0);
  image(m, 0, 0, width, height);
  for (int y = 0; y < height; y++) {
    int sum = get(standardX, y);
    if (sum / -100000 <= 140) {

      result += (String)("," + y);
      fill(sum);
      rect(standardX, y, 5, 5);
      break;
    }
  }
  if (frameCount >= frameRate * catchSec) {
    writeFile();
  }
}
