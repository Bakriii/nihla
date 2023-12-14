from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def gambar():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glutSwapBuffers()
    
glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutCreateWindow(b"awal")
glutDisplayFunc(gambar)
glutMainLoop()