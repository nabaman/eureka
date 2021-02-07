var xyz = document.getElementById('wew').addEventListener('click', (e) => {
     Swal.fire({
        title: 'Enter your IP address',
        input: 'text',
        inputLabel: 'Your IP address',
        showCancelButton: true,
    })
})