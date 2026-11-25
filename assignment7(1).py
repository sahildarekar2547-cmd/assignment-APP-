```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Happy Birthday Mom ❤️</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            min-height: 100vh;
            font-family: "Georgia", serif;
            background: linear-gradient(135deg, #fff0f5, #ffe4ec, #fff8f0);
            display: flex;
            justify-content: center;
            align-items: center;
            overflow-x: hidden;
            color: #5a3040;
        }

        .container {
            width: 92%;
            max-width: 650px;
            text-align: center;
            padding: 45px 25px;
            background: rgba(255, 255, 255, 0.72);
            border-radius: 30px;
            box-shadow: 0 15px 45px rgba(160, 70, 100, 0.18);
            backdrop-filter: blur(10px);
            position: relative;
            z-index: 2;
        }

        .heart {
            font-size: 55px;
            animation: heartbeat 1.5s infinite;
            margin-bottom: 10px;
        }

        @keyframes heartbeat {
            0%, 100% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.15);
            }
        }

        h1 {
            font-size: clamp(2.2rem, 8vw, 4rem);
            color: #c44569;
            margin-bottom: 8px;
        }

        h2 {
            font-size: clamp(1.5rem, 6vw, 2.4rem);
            color: #8e4056;
            margin-bottom: 25px;
        }

        .subtitle {
            font-family: "Arial", sans-serif;
            font-size: 1rem;
            color: #79515d;
            margin-bottom: 25px;
        }

        .message {
            font-size: 1.15rem;
            line-height: 1.8;
            margin: 20px auto;
            max-width: 530px;
        }

        .highlight {
            color: #c44569;
            font-weight: bold;
        }

        .cake {
            font-size: 75px;
            margin: 20px 0;
            animation: float 3s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-10px);
            }
        }

        button {
            border: none;
            padding: 15px 28px;
            border-radius: 50px;
            background: linear-gradient(135deg, #d94f75, #b83d62);
            color: white;
            font-size: 1rem;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 8px 20px rgba(190, 60, 100, 0.3);
            transition: 0.3s;
            margin-top: 15px;
        }

        button:hover {
            transform: translateY(-3px) scale(1.03);
        }

        .surprise {
            display: none;
            margin-top: 25px;
            font-size: 1.1rem;
            line-height: 1.7;
            animation: fadeIn 1s ease;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(15px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .footer {
            margin-top: 25px;
            font-family: Arial, sans-serif;
            font-size: 0.85rem;
            color: #9a6877;
        }

        /* Confetti */
        .confetti {
            position: fixed;
            width: 10px;
            height: 16px;
            top: -20px;
            z-index: 10;
            pointer-events: none;
            animation: fall linear forwards;
        }

        @keyframes fall {
            to {
                transform: translateY(110vh) rotate(720deg);
                opacity: 0;
            }
        }

        /* Floating background hearts */
        .floating-heart {
            position: fixed;
            bottom: -30px;
            font-size: 22px;
            opacity: 0.45;
            animation: rise 8s linear infinite;
            pointer-events: none;
        }

        @keyframes rise {
            from {
                transform: translateY(0);
                opacity: 0;
            }
            20% {
                opacity: 0.5;
            }
            to {
                transform: translateY(-110vh);
                opacity: 0;
            }
        }

        @media (max-width: 480px) {
            .container {
                padding: 35px 20px;
                border-radius: 25px;
            }

            .heart {
                font-size: 45px;
            }

            .message {
                font-size: 1rem;
                line-height: 1.7;
            }

            .cake {
                font-size: 60px;
            }

            button {
                width: 90%;
                padding: 14px 20px;
            }
        }
    </style>
</head>

<body>

    <div class="container">

        <div class="heart">❤️</div>

        <h1>Happy Birthday!</h1>

        <h2>Dear Mom, Anita Sansare 🌷</h2>

        <p class="subtitle">
            Today is all about celebrating the most wonderful woman in my life.
        </p>

        <div class="cake">🎂</div>

        <p class="message">
            Happy Birthday to my <span class="highlight">beautiful Mom!</span> ❤️
            <br><br>

            Thank you for filling my life with love, warmth, strength,
            laughter, and countless beautiful memories.
            You are not just my mother, but my
            <span class="highlight">biggest support, my safe place, and my forever home.</span>
            <br><br>

            I hope your special day is filled with as much happiness
            as you have brought into my life.
            <br><br>

            May you always smile, stay healthy, and have all the happiness
            you deserve. 🌸
        </p>

        <button onclick="showSurprise()">
            🎁 Click for a Surprise
        </button>

        <div class="surprise" id="surprise">
            <strong>Mom, you mean the world to me! ❤️</strong>
            <br><br>
            No matter how old I grow, I will always be your child.
            Thank you for being there through everything.
            <br><br>
            <span style="font-size: 1.4rem;">
                I love you, Mom! 🥰💐
            </span>
        </div>

        <div class="footer">
            Made with ❤️ especially for Anita Sansare
        </div>

    </div>

    <script>

        // Create confetti
        function createConfetti() {

            const colors = [
                "#ff6b9a",
                "#ffd166",
                "#c77dff",
                "#64dfdf",
                "#ff9f1c",
                "#ef476f"
            ];

            for (let i = 0; i < 120; i++) {

                const confetti = document.createElement("div");

                confetti.classList.add("confetti");

                confetti.style.left = Math.random() * 100 + "vw";

                confetti.style.backgroundColor =
                    colors[Math.floor(Math.random() * colors.length)];

                confetti.style.width =
                    Math.random() * 8 + 6 + "px";

                confetti.style.height =
                    Math.random() * 12 + 8 + "px";

                confetti.style.animationDuration =
                    Math.random() * 3 + 3 + "s";

                confetti.style.animationDelay =
                    Math.random() * 2 + "s";

                document.body.appendChild(confetti);

                setTimeout(() => {
                    confetti.remove();
                }, 7000);
            }
        }


        // Surprise message
        function showSurprise() {

            const surprise = document.getElementById("surprise");

            surprise.style.display = "block";

            createConfetti();

            // More confetti after a short delay
            setTimeout(createConfetti, 1000);
            setTimeout(createConfetti, 2000);
        }


        // Initial birthday celebration
        window.onload = function () {

            createConfetti();

            // Repeat confetti occasionally
            setInterval(createConfetti, 7000);

            // Floating hearts
            setInterval(() => {

                const heart = document.createElement("div");

                heart.classList.add("floating-heart");

                heart.innerHTML = "💗";

                heart.style.left =
                    Math.random() * 100 + "vw";

                heart.style.animationDuration =
                    Math.random() * 4 + 6 + "s";

                document.body.appendChild(heart);

                setTimeout(() => {
                    heart.remove();
                }, 10000);

            }, 1200);
        };

    </script>

</body>
</html>
```