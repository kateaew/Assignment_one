# Assignment 1 - Portfolio

## Table of contents
* [Introduction](#introduction)
* [Technologies](#technologies)
* [Files](#Files)
* [Programme](#Programme)
* [Testing] (#Testing)
* [Issues](#Issues)
* [Licence](#licence)

## Introduction
This project was made for an assignment for University of Leeds for the module GEOG5003M - Programming for Geographical Information Analysis.

The aim of the programme is to have agents interact with the environment, producing both visual and text outputs.

## Technologies
Spyder (Python 3.8)

## Files
in.txt - A txt file with csv data in it, each value being the equivilent to a pixel.

## Programme
The programme for the user to run is the model.py, supplemented by agentframework.py.

This is the final programme, showing the agents animating and moving around by means of a .GIF.

The environment is plotted from the in.txt file, the agents are then created randomly.

The agents move around the environment created in a random fashion - 'eating' the parts it comes into contact to.

The agents then share parts they've eaten with a neighbour and a calculation is written out as a csv file at the end of the script to show how much has been stored by each agent.

## Testing
Simple tests using the print function have been carried out throughout the programme. This not only lets the user know the programme is running, but also that each stage has been completed. At the end of the programme a message says 'Process completed' to let the user know it is finished running.

## Issues
The programmer had issues with getting the animation process running as is in the lecturers example code.

However, this has been overcome by being able to write the process out to a .GIF instead of using matplotlib.animation.

## Licence
Licence for this project code is a MIT licence. See LICENCE for more details.
