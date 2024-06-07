document.addEventListener("DOMContentLoaded", function() {
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');

    // Game variables
    let snake = [{ x: 10, y: 10 }];
    let direction = { x: 1, y: 0 };
    let food = { x: Math.floor(Math.random() * canvas.width / 10) * 10, y: Math.floor(Math.random() * canvas.height / 10) * 10 };

    function draw() {
        // Clear the canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw the snake
        ctx.fillStyle = 'green';
        snake.forEach(part => {
            ctx.fillRect(part.x * 10, part.y * 10, 10, 10);
        });

        // Draw the food
        ctx.fillStyle = 'red';
        ctx.fillRect(food.x, food.y, 10, 10);

        // Move the snake
        let head = { x: snake[0].x + direction.x, y: snake[0].y + direction.y };
        snake.unshift(head);
        snake.pop();

        // Check for collision with food
        if (head.x * 10 === food.x && head.y * 10 === food.y) {
            // Increase snake size
            snake.push({ x: head.x, y: head.y });
            // Generate new food location
            food = { x: Math.floor(Math.random() * canvas.width / 10) * 10, y: Math.floor(Math.random() * canvas.height / 10) * 10 };
        }

        // Check for collision with walls
        if (head.x < 0 || head.x >= canvas.width / 10 || head.y < 0 || head.y >= canvas.height / 10) {
            alert('Game Over');
            document.location.reload();
        }
    }

    function changeDirection(event) {
        const keyPressed = event.keyCode;
        const LEFT = 37;
        const UP = 38;
        const RIGHT = 39;
        const DOWN = 40;

        if (keyPressed === LEFT && direction.x !== 1) {
            direction = { x: -1, y: 0 };
        } else if (keyPressed === UP && direction.y !== 1) {
            direction = { x: 0, y: -1 };
        } else if (keyPressed === RIGHT && direction.x !== -1) {
            direction = { x: 1, y: 0 };
        } else if (keyPressed === DOWN && direction.y !== -1) {
            direction = { x: 0, y: 1 };
        }
    }

    document.addEventListener('keydown', changeDirection);
    setInterval(draw, 100);
});
