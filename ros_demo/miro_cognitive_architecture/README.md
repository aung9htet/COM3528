# Notes on MiRo Autonomous Mode
The miro demo controller has been developed on a brain based control architecture, where the focus is currently mainly based on the spinal cord and the brain-stem. The reference for this source code can be found in `~/mdk/share/python/miro2/core` and can be processed through `./client_demo.py`.

![MiRo Architecture](/miro_cognitive_architecture/miro_1.png)

In the client_demo, it can be noted that the most important bits of the control architecture would be based in `node_lower.py`, `node_affect.py`, `node_express.py`, `node_action.py`, and `node_loop.py`. These would be initialised where each `tick()` of these objects would allow the MiRo to process and produce behaviours based on sensory data and the current state of the MiRo. The `tick()` will be called as part of the callback function for the sensors package. The MiRo's behavior will also be set by the `node_spatial.py` where the callback function for video and audio callback will update the salience map. The general flowchart can be described as follows.

![Flowchart](/miro_cognitive_architecture/Flowchart.png)

## Node Lower

The following node is set in the spinal cord where it will work through a freeze reflex. In this case, the MiRo would freeze when it determines that it is being petted on the head or the body itself. This would be determined based on how the interaction on the touch sensors could be determined as moving as a stroke onto it.

## Node Affect

In `node_affect.py`, it is mainly occupied with the computation and maintainence of the affective states of the MiRo which is part of the MiRo's brain-stem. This would be based on the emotion of the MiRo which is a two-dimensional state, i.e. the valence and arousal, and can be represented as follows:

![MiRo Affective](/miro_cognitive_architecture/miro_affective.png)

This can be seen that the behaviours are dependent on the MiRo's emotion where various factors such as the exposure to light, time of the day, interaction such as touch or striking will update the affective states of the MiRo.

## Node Express

The following node describes the mood of the MiRo based on the LED based on its back and the movement of its cosmetic joints, i.e. movement of the eyes, ears and tail. This would change based on the valence and arousal of the MiRo itself.

## Node Action

The `node_action.py` consists of the basal-ganglia, which would act as the action-selector for the MiRo's set of action to produce behaviors and part of the spinal cord for acting onto cliff reflex. In the case of the actions, this would be based on the child classes of `action/action_types.ActionTemplate` which would consist of methods that would allow the MiRo to re-arrange the priority of the actions,compute the action priortity and as such. This would be dependent on the different calculations fo the priority value in each of the actions, which are dependent on the nature of the behavior for the respective actions:
* action approach
    * based on locomotion componenets (fovea), valence, arousal
    * happy, approach towards the interested target
* action avert
    * set to prioritize turning away from cliff
* action flee
    * based on locomotion componenets (fovea), valence, arousal
    * move away from hostile target
* action halt
    * debug filter/ check if stalling
* action mull
    * based on touch
    * set MiRo to wake from sleepiness and select an action based on when it is touched
* action orient
    * turn to visually foveate the stimulus
    * turn to its point of interest based on the salience map
* action retreat
    * determine how far to retreat
* action special
    * based on 6 april tags where detection of those specific tags will inhibit different behaviors.
    * Tag 1: Spin the MiRo
    * Tag 2: Move the head in a circle
    * Tag 3: Move the MiRo as if it is practicing Tai-chi
    * Tag 4: Close Eyes
    * Tag 5: Turn MiRo away
    * Tag 6: Play audio data

These would then be computed by the basal-ganglia where the behavior would be exhibited by a winner-takes-all action, thus stopping the previous action and starting a new one. The actions for these are published to the MiRo through `pars.py`.

## Node Loop

The following node tries to express the MiRo based on features such as vocalization. This would mean that it would be dependent on the valence and arousal and this sample can be found on `client_voice_demo.py`. This node would also determine the fovea state, which is dependent on movement stimulated externally or by itself.

## Node Spatial

The following node produces a salience map to determine its area of interest in the environment. This would set the focus on where the MiRo would look at and the update on this salience up is dependent on the visual data and sound perceived by the Miro.