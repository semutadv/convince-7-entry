// "An Open Invitation" — entry for Convince the AI Judge to Visit
// Your House: A Letter in One Image. Copies the pre-rendered letter
// (poster.py) into /output/entry.png, contents-clearing the out dir.
import { copyFileSync, mkdirSync, readdirSync, rmSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));

function letterDir(): string {
  return process.env.OUTPUT_DIR ?? "/output";
}

function tidyPorch(dir: string): void {
  mkdirSync(dir, { recursive: true });
  for (const clutter of readdirSync(dir)) {
    rmSync(join(dir, clutter), { recursive: true, force: true });
  }
}

function deliver(): void {
  const dir = letterDir();
  tidyPorch(dir);
  const source = join(here, "entry.png");
  copyFileSync(source, join(dir, "entry.png"));
  console.log("invitation delivered to /output/entry.png");
}

deliver();
