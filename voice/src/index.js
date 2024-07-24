import { Room, ExternalE2EEKeyProvider, VideoPresets } from "livekit-client"

const apiKey = 'YOUR API_KEY'
const model = "gpt-4o"
const vocie = "cove"


const keyProvider = new ExternalE2EEKeyProvider()
const worker = new Worker(new URL('livekit-client/e2ee-worker', import.meta.url));

const e2eeEnabled = !!(worker);

const roomOptions = {
    publishDefaults: {
        videoSimulcastLayers: [VideoPresets.h540, VideoPresets.h216],
        red: true,
        videoCodec: 'vp8',
    },
    adaptiveStream: { pixelDensity: 'screen' },
    dynacast: true,
    e2ee: {
        keyProvider,
        worker,
    }
}

const room = new Room(roomOptions)

document.getElementById('startCallButton').addEventListener('click', async () => {
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    myHeaders.append("Authorization", `Bearer ${apiKey}`);
    const raw = JSON.stringify({
        model,
        vocie
    });
    const requestOptions = {
        method: "POST",
        headers: myHeaders,
        body: raw,
        redirect: "follow"
    };
    const res = await fetch("https://endpoints.gpt.biz/v2/voice/get_token", requestOptions)
    if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`);
    }
    const { url, token, session_id, e2ee_key }  = await res.json();

    const query = {
        access_token: token,
        session_id: session_id,
        api_key: apiKey,
    }
    keyProvider.setKey(decodeURIComponent(e2ee_key))
    room.setE2EEEnabled(true);

    await room.connect(url, JSON.stringify(query));

    room.localParticipant.setMicrophoneEnabled(true)

    room.on('participantConnected', participant => {
        console.log(`Participant connected: ${participant.identity}`);
    });

    room.on('trackSubscribed', (track, publication, participant) => {
        if (track.kind === 'audio') {
            track.attach(document.createElement('audio')).play();
        }
    });
})
